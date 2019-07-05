﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import json
from typing import TYPE_CHECKING, Dict, Any, Optional


from azure.core.exceptions import HttpResponseError


if TYPE_CHECKING:
    from azure.core.pipeline.transport.base import _HttpResponseBase


class ODataV4Error(HttpResponseError):
    """An HTTP response error where the JSON is decoded as OData V4 error format.

    http://docs.oasis-open.org/odata/odata-json-format/v4.0/os/odata-json-format-v4.0-os.html#_Toc372793091

    :ivar dict odata_json: The parsed JSON body as attribute for convenience.
    :ivar str code: Its value is a service-defined error code. This code serves as a sub-status for the HTTP error code specified in the response.
    :ivar str message: Human-readable, language-dependent representation of the error.
    :ivar str target: The target of the particular error (for example, the name of the property in error).
    :ivar list details: Array of JSON objects that MUST contain name/value pairs for code and message, and MAY contain a name/value pair for target, as described above.
    :ivar dict innererror: An object. The contents of this object are service-defined. Usually this object contains information that will help debug the service.
    """

    def __init__(self, response, **kwargs):
        # type: (_HttpResponseBase, Dict[str, Any]) -> None

        # Ensure field are declared, whatever can happen afterwards
        self.odata_json = None  # type: Optional[dict[str, Any]]
        try:
            self.odata_json = json.loads(response.body())
            odata_message = self.odata_json.setdefault("error", {}).get("message")
        except Exception:
            # If the body is not JSON valid, just stop now
            odata_message = None

        self.code = None  # type: Optional[str]
        self.message = kwargs.get("message", odata_message)  # type: Optional[str]
        self.target = None  # type: Optional[str]
        self.details = []  # type: Optional[List[Any]]
        self.innererror = {}  # type: Optional[Dict[str, Any]]

        super(ODataV4Error, self).__init__(
            response=response, **kwargs
        )

        # Required fields, but assume they could be missing still to be robust
        try:
            error_node = self.odata_json.get("error")
            self.code = error_node.get("code")

            # Optional fields
            self.target = error_node.get("target", None)  # type: str
            self.details = error_node.get("details", [])  # type: List[Dict[str, Any]]
            self.innererror = error_node.get("innererror", {})  # type: Dict[str, Any]
        except Exception:
            # No details, too bad...
            pass



class TypedErrorInfo:
    """Additional info class defined in ARM specification.

    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-details.md#error-response-content
    """

    def __init__(self, type, info):
        self.type = type
        self.info = info

    def __str__(self):
        """Cloud error message."""
        error_str = "Type: {}".format(self.type)
        error_str += "\nInfo: {}".format(json.dumps(self.info, indent=4))
        return error_str


class ARMErrorFormat:
    """Describe error format from ARM, used at the base or inside "details" node.

    This format is compatible with ODataV4 format.
    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-details.md#error-response-content
    """

    def __init__(self, json_object):
        # Required fields, but assume they could be missing still to be robust
        self.code = json_object.get("code")  # type: Optional[str]
        self.message = json_object.get("message")  # type: Optional[str]

        # Optional fields
        self.target = json_object.get("target", None)  # type: str

        # details is recursive of this very format
        self.details = [
            ARMErrorFormat(detail_node)
            for detail_node in json_object.get("details", [])
        ]  # type: List[ARMErrorFormat]

        # innererror is not mentioned in ARM spec, keep it for consistency with OData v4
        self.innererror = json_object.get("innererror", None)  # type: Dict[str, Any]

        # ARM specific annotations
        self.additional_info = [
            TypedErrorInfo(additional_info["type"], additional_info["info"])
            for additional_info in json_object.get("additionalInfo", [])
        ]

    def __str__(self):
        error_str = "Code: {}".format(self.code)
        error_str += "\nMessage: {}".format(self.message)
        if self.target:
            error_str += "\nTarget: {}".format(self.target)

        if self.details:
            error_str += "\nException Details:"
            for error_obj in self.details:
                # Indent for visibility
                error_str += "\n".join("\t" + s for s in str(error_obj).splitlines())

        if self.innererror:
            error_str += "\nInner error: {}".format(
                json.dumps(self.innererror, indent=4)
            )

        if self.additional_info:
            error_str += "\nAdditional Information:"
            for error_info in self.additional_info:
                error_str += str(error_info)

        return error_str


class ARMError(ODataV4Error):
    """An HTTP error from an ARM endpoint.

    This subclass ODataV4Error since ARM specifications requires all
    ARM error to be complient with it.

    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-details.md#error-response-content
    """

    def __init__(self, response, **kwargs):
        # type: (_HttpResponseBase, Dict[str, Any]) -> None
        super(ARMError, self).__init__(response=response, **kwargs)

        if self.odata_json:
            try:
                error_node = self.odata_json["error"]
                self._arm_error_format = ARMErrorFormat(error_node)
                # ARM error format is more typed than OData v4, replace, but keep message
                self.__dict__.update(self._arm_error_format.__dict__)
            except Exception:
                pass

        if "message" in kwargs:
            self.message = kwargs["message"]

    def __str__(self):
        return str(self._arm_error_format)