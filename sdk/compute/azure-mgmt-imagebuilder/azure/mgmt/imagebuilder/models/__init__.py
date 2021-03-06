# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApiError, ApiErrorException
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import ImageTemplate
    from ._models_py3 import ImageTemplateCustomizer
    from ._models_py3 import ImageTemplateDistributor
    from ._models_py3 import ImageTemplateFileCustomizer
    from ._models_py3 import ImageTemplateIdentity
    from ._models_py3 import ImageTemplateIdentityUserAssignedIdentitiesValue
    from ._models_py3 import ImageTemplateIsoSource
    from ._models_py3 import ImageTemplateLastRunStatus
    from ._models_py3 import ImageTemplateManagedImageDistributor
    from ._models_py3 import ImageTemplateManagedImageSource
    from ._models_py3 import ImageTemplatePlatformImageSource
    from ._models_py3 import ImageTemplatePowerShellCustomizer
    from ._models_py3 import ImageTemplateRestartCustomizer
    from ._models_py3 import ImageTemplateSharedImageDistributor
    from ._models_py3 import ImageTemplateSharedImageVersionSource
    from ._models_py3 import ImageTemplateShellCustomizer
    from ._models_py3 import ImageTemplateSource
    from ._models_py3 import ImageTemplateUpdateParameters
    from ._models_py3 import ImageTemplateVhdDistributor
    from ._models_py3 import ImageTemplateVmProfile
    from ._models_py3 import InnerError
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProvisioningError
    from ._models_py3 import Resource
    from ._models_py3 import RunOutput
    from ._models_py3 import SubResource
except (SyntaxError, ImportError):
    from ._models import ApiError, ApiErrorException
    from ._models import ApiErrorBase
    from ._models import ImageTemplate
    from ._models import ImageTemplateCustomizer
    from ._models import ImageTemplateDistributor
    from ._models import ImageTemplateFileCustomizer
    from ._models import ImageTemplateIdentity
    from ._models import ImageTemplateIdentityUserAssignedIdentitiesValue
    from ._models import ImageTemplateIsoSource
    from ._models import ImageTemplateLastRunStatus
    from ._models import ImageTemplateManagedImageDistributor
    from ._models import ImageTemplateManagedImageSource
    from ._models import ImageTemplatePlatformImageSource
    from ._models import ImageTemplatePowerShellCustomizer
    from ._models import ImageTemplateRestartCustomizer
    from ._models import ImageTemplateSharedImageDistributor
    from ._models import ImageTemplateSharedImageVersionSource
    from ._models import ImageTemplateShellCustomizer
    from ._models import ImageTemplateSource
    from ._models import ImageTemplateUpdateParameters
    from ._models import ImageTemplateVhdDistributor
    from ._models import ImageTemplateVmProfile
    from ._models import InnerError
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ProvisioningError
    from ._models import Resource
    from ._models import RunOutput
    from ._models import SubResource
from ._paged_models import ImageTemplatePaged
from ._paged_models import OperationPaged
from ._paged_models import RunOutputPaged
from ._image_builder_client_enums import (
    ProvisioningState,
    ProvisioningErrorCode,
    RunState,
    RunSubState,
    ResourceIdentityType,
)

__all__ = [
    'ApiError', 'ApiErrorException',
    'ApiErrorBase',
    'ImageTemplate',
    'ImageTemplateCustomizer',
    'ImageTemplateDistributor',
    'ImageTemplateFileCustomizer',
    'ImageTemplateIdentity',
    'ImageTemplateIdentityUserAssignedIdentitiesValue',
    'ImageTemplateIsoSource',
    'ImageTemplateLastRunStatus',
    'ImageTemplateManagedImageDistributor',
    'ImageTemplateManagedImageSource',
    'ImageTemplatePlatformImageSource',
    'ImageTemplatePowerShellCustomizer',
    'ImageTemplateRestartCustomizer',
    'ImageTemplateSharedImageDistributor',
    'ImageTemplateSharedImageVersionSource',
    'ImageTemplateShellCustomizer',
    'ImageTemplateSource',
    'ImageTemplateUpdateParameters',
    'ImageTemplateVhdDistributor',
    'ImageTemplateVmProfile',
    'InnerError',
    'Operation',
    'OperationDisplay',
    'ProvisioningError',
    'Resource',
    'RunOutput',
    'SubResource',
    'ImageTemplatePaged',
    'RunOutputPaged',
    'OperationPaged',
    'ProvisioningState',
    'ProvisioningErrorCode',
    'RunState',
    'RunSubState',
    'ResourceIdentityType',
]
