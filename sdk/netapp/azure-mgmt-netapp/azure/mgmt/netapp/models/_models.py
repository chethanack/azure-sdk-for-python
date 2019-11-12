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

from msrest.serialization import Model


class ActiveDirectory(Model):
    """Active Directory.

    :param active_directory_id: Id of the Active Directory
    :type active_directory_id: str
    :param username: Username of Active Directory domain administrator
    :type username: str
    :param password: Plain text password of Active Directory domain
     administrator
    :type password: str
    :param domain: Name of the Active Directory domain
    :type domain: str
    :param dns: Comma separated list of DNS server IP addresses (IPv4 only)
     for the Active Directory domain
    :type dns: str
    :param status: Status of the Active Directory
    :type status: str
    :param smb_server_name: NetBIOS name of the SMB server. This name will be
     registered as a computer account in the AD and used to mount volumes
    :type smb_server_name: str
    :param organizational_unit: The Organizational Unit (OU) within the
     Windows Active Directory
    :type organizational_unit: str
    """

    _attribute_map = {
        'active_directory_id': {'key': 'activeDirectoryId', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'dns': {'key': 'dns', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'smb_server_name': {'key': 'smbServerName', 'type': 'str'},
        'organizational_unit': {'key': 'organizationalUnit', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ActiveDirectory, self).__init__(**kwargs)
        self.active_directory_id = kwargs.get('active_directory_id', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.domain = kwargs.get('domain', None)
        self.dns = kwargs.get('dns', None)
        self.status = kwargs.get('status', None)
        self.smb_server_name = kwargs.get('smb_server_name', None)
        self.organizational_unit = kwargs.get('organizational_unit', None)


class CapacityPool(Model):
    """Capacity pool resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar pool_id: poolId. UUID v4 used to identify the Pool
    :vartype pool_id: str
    :param size: Required. size. Provisioned size of the pool (in bytes).
     Allowed values are in 4TiB chunks (value must be multiply of
     4398046511104).
    :type size: long
    :param service_level: Required. serviceLevel. The service level of the
     file system. Possible values include: 'Standard', 'Premium', 'Ultra'.
     Default value: "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'pool_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'size': {'required': True, 'maximum': 549755813888000, 'minimum': 4398046511104},
        'service_level': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'pool_id': {'key': 'properties.poolId', 'type': 'str'},
        'size': {'key': 'properties.size', 'type': 'long'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CapacityPool, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.pool_id = None
        self.size = kwargs.get('size', None)
        self.service_level = kwargs.get('service_level', "Premium")
        self.provisioning_state = None


class CapacityPoolPatch(Model):
    """Capacity pool patch resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param size: size. Provisioned size of the pool (in bytes). Allowed values
     are in 4TiB chunks (value must be multiply of 4398046511104). Default
     value: 4398046511104 .
    :type size: long
    :param service_level: serviceLevel. The service level of the file system.
     Possible values include: 'Standard', 'Premium', 'Ultra'. Default value:
     "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'size': {'maximum': 549755813888000, 'minimum': 4398046511104},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'size': {'key': 'properties.size', 'type': 'long'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CapacityPoolPatch, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.size = kwargs.get('size', 4398046511104)
        self.service_level = kwargs.get('service_level', "Premium")


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Dimension(Model):
    """Dimension of blobs, possibly be blob type or access tier.

    :param name: Display name of dimension.
    :type name: str
    :param display_name: Display name of dimension.
    :type display_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Dimension, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)


class ExportPolicyRule(Model):
    """Volume Export Policy Rule.

    :param rule_index: Order index
    :type rule_index: int
    :param unix_read_only: Read only access
    :type unix_read_only: bool
    :param unix_read_write: Read and write access
    :type unix_read_write: bool
    :param cifs: Allows CIFS protocol
    :type cifs: bool
    :param nfsv3: Allows NFSv3 protocol
    :type nfsv3: bool
    :param nfsv41: Allows NFSv4.1 protocol
    :type nfsv41: bool
    :param allowed_clients: Client ingress specification as comma separated
     string with IPv4 CIDRs, IPv4 host addresses and host names
    :type allowed_clients: str
    """

    _attribute_map = {
        'rule_index': {'key': 'ruleIndex', 'type': 'int'},
        'unix_read_only': {'key': 'unixReadOnly', 'type': 'bool'},
        'unix_read_write': {'key': 'unixReadWrite', 'type': 'bool'},
        'cifs': {'key': 'cifs', 'type': 'bool'},
        'nfsv3': {'key': 'nfsv3', 'type': 'bool'},
        'nfsv41': {'key': 'nfsv41', 'type': 'bool'},
        'allowed_clients': {'key': 'allowedClients', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExportPolicyRule, self).__init__(**kwargs)
        self.rule_index = kwargs.get('rule_index', None)
        self.unix_read_only = kwargs.get('unix_read_only', None)
        self.unix_read_write = kwargs.get('unix_read_write', None)
        self.cifs = kwargs.get('cifs', None)
        self.nfsv3 = kwargs.get('nfsv3', None)
        self.nfsv41 = kwargs.get('nfsv41', None)
        self.allowed_clients = kwargs.get('allowed_clients', None)


class MetricSpecification(Model):
    """Metric specification of operation.

    :param name: Name of metric specification.
    :type name: str
    :param display_name: Display name of metric specification.
    :type display_name: str
    :param display_description: Display description of metric specification.
    :type display_description: str
    :param unit: Unit could be Bytes or Count.
    :type unit: str
    :param dimensions: Dimensions of blobs, including blob type and access
     tier.
    :type dimensions: list[~azure.mgmt.netapp.models.Dimension]
    :param aggregation_type: Aggregation type could be Average.
    :type aggregation_type: str
    :param fill_gap_with_zero: The property to decide fill gap with zero or
     not.
    :type fill_gap_with_zero: bool
    :param category: The category this metric specification belong to, could
     be Capacity.
    :type category: str
    :param resource_id_dimension_name_override: Account Resource Id.
    :type resource_id_dimension_name_override: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'display_description': {'key': 'displayDescription', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
        'aggregation_type': {'key': 'aggregationType', 'type': 'str'},
        'fill_gap_with_zero': {'key': 'fillGapWithZero', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'resource_id_dimension_name_override': {'key': 'resourceIdDimensionNameOverride', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MetricSpecification, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.display_description = kwargs.get('display_description', None)
        self.unit = kwargs.get('unit', None)
        self.dimensions = kwargs.get('dimensions', None)
        self.aggregation_type = kwargs.get('aggregation_type', None)
        self.fill_gap_with_zero = kwargs.get('fill_gap_with_zero', None)
        self.category = kwargs.get('category', None)
        self.resource_id_dimension_name_override = kwargs.get('resource_id_dimension_name_override', None)


class MountTarget(Model):
    """Mount Target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar mount_target_id: mountTargetId. UUID v4 used to identify the
     MountTarget
    :vartype mount_target_id: str
    :param file_system_id: Required. fileSystemId. UUID v4 used to identify
     the MountTarget
    :type file_system_id: str
    :ivar ip_address: ipAddress. The mount target's IPv4 address
    :vartype ip_address: str
    :param subnet: subnet. The subnet
    :type subnet: str
    :param start_ip: startIp. The start of IPv4 address range to use when
     creating a new mount target
    :type start_ip: str
    :param end_ip: endIp. The end of IPv4 address range to use when creating a
     new mount target
    :type end_ip: str
    :param gateway: gateway. The gateway of the IPv4 address range to use when
     creating a new mount target
    :type gateway: str
    :param netmask: netmask. The netmask of the IPv4 address range to use when
     creating a new mount target
    :type netmask: str
    :param smb_server_fqdn: smbServerFQDN. The SMB server's Fully Qualified
     Domain Name, FQDN
    :type smb_server_fqdn: str
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'mount_target_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'file_system_id': {'required': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'ip_address': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'mount_target_id': {'key': 'properties.mountTargetId', 'type': 'str'},
        'file_system_id': {'key': 'properties.fileSystemId', 'type': 'str'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'str'},
        'start_ip': {'key': 'properties.startIp', 'type': 'str'},
        'end_ip': {'key': 'properties.endIp', 'type': 'str'},
        'gateway': {'key': 'properties.gateway', 'type': 'str'},
        'netmask': {'key': 'properties.netmask', 'type': 'str'},
        'smb_server_fqdn': {'key': 'properties.smbServerFqdn', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MountTarget, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.mount_target_id = None
        self.file_system_id = kwargs.get('file_system_id', None)
        self.ip_address = None
        self.subnet = kwargs.get('subnet', None)
        self.start_ip = kwargs.get('start_ip', None)
        self.end_ip = kwargs.get('end_ip', None)
        self.gateway = kwargs.get('gateway', None)
        self.netmask = kwargs.get('netmask', None)
        self.smb_server_fqdn = kwargs.get('smb_server_fqdn', None)
        self.provisioning_state = None


class NetAppAccount(Model):
    """NetApp account resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    :param active_directories: Active Directories
    :type active_directories: list[~azure.mgmt.netapp.models.ActiveDirectory]
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'active_directories': {'key': 'properties.activeDirectories', 'type': '[ActiveDirectory]'},
    }

    def __init__(self, **kwargs):
        super(NetAppAccount, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.provisioning_state = None
        self.active_directories = kwargs.get('active_directories', None)


class NetAppAccountPatch(Model):
    """NetApp account patch resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    :param active_directories: Active Directories
    :type active_directories: list[~azure.mgmt.netapp.models.ActiveDirectory]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'active_directories': {'key': 'properties.activeDirectories', 'type': '[ActiveDirectory]'},
    }

    def __init__(self, **kwargs):
        super(NetAppAccountPatch, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.provisioning_state = None
        self.active_directories = kwargs.get('active_directories', None)


class Operation(Model):
    """Microsoft.NetApp REST API operation definition.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.netapp.models.OperationDisplay
    :param origin: The origin of operations.
    :type origin: str
    :param service_specification: One property of operation, include metric
     specifications.
    :type service_specification:
     ~azure.mgmt.netapp.models.ServiceSpecification
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.service_specification = kwargs.get('service_specification', None)


class OperationDisplay(Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft NetApp.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ReplicationObject(Model):
    """Replication properties.

    All required parameters must be populated in order to send to Azure.

    :param replication_id: replicationId. Id
    :type replication_id: str
    :param endpoint_type: Required. endpointType. Indicates whether the local
     volume is the source or destination for the Volume Replication
    :type endpoint_type: str
    :param replication_schedule: Required. replicationSchedule. Schedule
    :type replication_schedule: str
    :param remote_volume_resource_id: Required. remoteVolumeResourceId. The
     resource ID of the remote volume.
    :type remote_volume_resource_id: str
    """

    _validation = {
        'endpoint_type': {'required': True},
        'replication_schedule': {'required': True},
        'remote_volume_resource_id': {'required': True},
    }

    _attribute_map = {
        'replication_id': {'key': 'replicationId', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'replication_schedule': {'key': 'replicationSchedule', 'type': 'str'},
        'remote_volume_resource_id': {'key': 'remoteVolumeResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ReplicationObject, self).__init__(**kwargs)
        self.replication_id = kwargs.get('replication_id', None)
        self.endpoint_type = kwargs.get('endpoint_type', None)
        self.replication_schedule = kwargs.get('replication_schedule', None)
        self.remote_volume_resource_id = kwargs.get('remote_volume_resource_id', None)


class ResourceNameAvailability(Model):
    """Information regarding availability of a resource name.

    :param is_available: <code>true</code> indicates name is valid and
     available. <code>false</code> indicates the name is invalid, unavailable,
     or both.
    :type is_available: bool
    :param reason: <code>Invalid</code> indicates the name provided does not
     match Azure App Service naming requirements. <code>AlreadyExists</code>
     indicates that the name is already in use and is therefore unavailable.
     Possible values include: 'Invalid', 'AlreadyExists'
    :type reason: str or ~azure.mgmt.netapp.models.InAvailabilityReasonType
    :param message: If reason == invalid, provide the user with the reason why
     the given name is invalid, and provide the resource naming requirements so
     that the user can select a valid name. If reason == AlreadyExists, explain
     that resource name is already in use, and direct them to select a
     different name.
    :type message: str
    """

    _attribute_map = {
        'is_available': {'key': 'isAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceNameAvailability, self).__init__(**kwargs)
        self.is_available = kwargs.get('is_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class ResourceNameAvailabilityRequest(Model):
    """Resource name availability request content.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Resource name to verify.
    :type name: str
    :param type: Required. Resource type used for verification. Possible
     values include: 'Microsoft.NetApp/netAppAccounts',
     'Microsoft.NetApp/netAppAccounts/capacityPools',
     'Microsoft.NetApp/netAppAccounts/capacityPools/volumes',
     'Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots'
    :type type: str or ~azure.mgmt.netapp.models.CheckNameResourceTypes
    :param resource_group: Required. Resource group name.
    :type resource_group: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'resource_group': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceNameAvailabilityRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.resource_group = kwargs.get('resource_group', None)


class ServiceSpecification(Model):
    """One property of operation, include metric specifications.

    :param metric_specifications: Metric specifications of operation.
    :type metric_specifications:
     list[~azure.mgmt.netapp.models.MetricSpecification]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
    }

    def __init__(self, **kwargs):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = kwargs.get('metric_specifications', None)


class Snapshot(Model):
    """Snapshot of a Volume.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar snapshot_id: snapshotId. UUID v4 used to identify the Snapshot
    :vartype snapshot_id: str
    :param file_system_id: fileSystemId. UUID v4 used to identify the
     FileSystem
    :type file_system_id: str
    :ivar created: name. The creation date of the snapshot
    :vartype created: datetime
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'snapshot_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'file_system_id': {'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'created': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'snapshot_id': {'key': 'properties.snapshotId', 'type': 'str'},
        'file_system_id': {'key': 'properties.fileSystemId', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Snapshot, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.snapshot_id = None
        self.file_system_id = kwargs.get('file_system_id', None)
        self.created = None
        self.provisioning_state = None


class SnapshotPatch(Model):
    """Snapshot patch.

    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(SnapshotPatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class Volume(Model):
    """Volume resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar file_system_id: FileSystem ID. Unique FileSystem Identifier.
    :vartype file_system_id: str
    :param creation_token: Required. Creation Token or File Path. A unique
     file path for the volume. Used when creating mount targets
    :type creation_token: str
    :param service_level: serviceLevel. The service level of the file system.
     Possible values include: 'Standard', 'Premium', 'Ultra'. Default value:
     "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    :param usage_threshold: Required. usageThreshold. Maximum storage quota
     allowed for a file system in bytes. This is a soft quota used for alerting
     only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
     Default value: 107374182400 .
    :type usage_threshold: long
    :param export_policy: exportPolicy. Set of export policy rules
    :type export_policy:
     ~azure.mgmt.netapp.models.VolumePropertiesExportPolicy
    :param protocol_types: protocolTypes. Set of protocol types
    :type protocol_types: list[str]
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    :param snapshot_id: Snapshot ID. UUID v4 or resource identifier used to
     identify the Snapshot.
    :type snapshot_id: str
    :ivar baremetal_tenant_id: Baremetal Tenant ID. Unique Baremetal Tenant
     Identifier.
    :vartype baremetal_tenant_id: str
    :param subnet_id: Required. The Azure Resource URI for a delegated subnet.
     Must have the delegation Microsoft.NetApp/volumes
    :type subnet_id: str
    :param mount_targets: mountTargets. List of mount targets
    :type mount_targets: object
    :param volume_type: What type of volume is this
    :type volume_type: str
    :param data_protection: DataProtection. DataProtection volume, can have a
     replication object
    :type data_protection:
     ~azure.mgmt.netapp.models.VolumePropertiesDataProtection
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'file_system_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'creation_token': {'required': True},
        'usage_threshold': {'required': True, 'maximum': 109951162777600, 'minimum': 107374182400},
        'provisioning_state': {'readonly': True},
        'snapshot_id': {'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}|(\\?([^\/]*[\/])*)([^\/]+)$'},
        'baremetal_tenant_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'subnet_id': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'file_system_id': {'key': 'properties.fileSystemId', 'type': 'str'},
        'creation_token': {'key': 'properties.creationToken', 'type': 'str'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
        'usage_threshold': {'key': 'properties.usageThreshold', 'type': 'long'},
        'export_policy': {'key': 'properties.exportPolicy', 'type': 'VolumePropertiesExportPolicy'},
        'protocol_types': {'key': 'properties.protocolTypes', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'snapshot_id': {'key': 'properties.snapshotId', 'type': 'str'},
        'baremetal_tenant_id': {'key': 'properties.baremetalTenantId', 'type': 'str'},
        'subnet_id': {'key': 'properties.subnetId', 'type': 'str'},
        'mount_targets': {'key': 'properties.mountTargets', 'type': 'object'},
        'volume_type': {'key': 'properties.volumeType', 'type': 'str'},
        'data_protection': {'key': 'properties.dataProtection', 'type': 'VolumePropertiesDataProtection'},
    }

    def __init__(self, **kwargs):
        super(Volume, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.file_system_id = None
        self.creation_token = kwargs.get('creation_token', None)
        self.service_level = kwargs.get('service_level', "Premium")
        self.usage_threshold = kwargs.get('usage_threshold', 107374182400)
        self.export_policy = kwargs.get('export_policy', None)
        self.protocol_types = kwargs.get('protocol_types', None)
        self.provisioning_state = None
        self.snapshot_id = kwargs.get('snapshot_id', None)
        self.baremetal_tenant_id = None
        self.subnet_id = kwargs.get('subnet_id', None)
        self.mount_targets = kwargs.get('mount_targets', None)
        self.volume_type = kwargs.get('volume_type', None)
        self.data_protection = kwargs.get('data_protection', None)


class VolumePatch(Model):
    """Volume patch resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param service_level: serviceLevel. The service level of the file system.
     Possible values include: 'Standard', 'Premium', 'Ultra'. Default value:
     "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    :param usage_threshold: usageThreshold. Maximum storage quota allowed for
     a file system in bytes. This is a soft quota used for alerting only.
     Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
     Default value: 107374182400 .
    :type usage_threshold: long
    :param export_policy: exportPolicy. Set of export policy rules
    :type export_policy:
     ~azure.mgmt.netapp.models.VolumePatchPropertiesExportPolicy
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'usage_threshold': {'maximum': 109951162777600, 'minimum': 107374182400},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
        'usage_threshold': {'key': 'properties.usageThreshold', 'type': 'long'},
        'export_policy': {'key': 'properties.exportPolicy', 'type': 'VolumePatchPropertiesExportPolicy'},
    }

    def __init__(self, **kwargs):
        super(VolumePatch, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.service_level = kwargs.get('service_level', "Premium")
        self.usage_threshold = kwargs.get('usage_threshold', 107374182400)
        self.export_policy = kwargs.get('export_policy', None)


class VolumePatchPropertiesExportPolicy(Model):
    """exportPolicy.

    Set of export policy rules.

    :param rules: Export policy rule. Export policy rule
    :type rules: list[~azure.mgmt.netapp.models.ExportPolicyRule]
    """

    _attribute_map = {
        'rules': {'key': 'rules', 'type': '[ExportPolicyRule]'},
    }

    def __init__(self, **kwargs):
        super(VolumePatchPropertiesExportPolicy, self).__init__(**kwargs)
        self.rules = kwargs.get('rules', None)


class VolumePropertiesDataProtection(Model):
    """DataProtection.

    DataProtection volume, can have a replication object.

    :param replication: Replication. Replication properties
    :type replication: ~azure.mgmt.netapp.models.ReplicationObject
    """

    _attribute_map = {
        'replication': {'key': 'replication', 'type': 'ReplicationObject'},
    }

    def __init__(self, **kwargs):
        super(VolumePropertiesDataProtection, self).__init__(**kwargs)
        self.replication = kwargs.get('replication', None)


class VolumePropertiesExportPolicy(Model):
    """exportPolicy.

    Set of export policy rules.

    :param rules: Export policy rule. Export policy rule
    :type rules: list[~azure.mgmt.netapp.models.ExportPolicyRule]
    """

    _attribute_map = {
        'rules': {'key': 'rules', 'type': '[ExportPolicyRule]'},
    }

    def __init__(self, **kwargs):
        super(VolumePropertiesExportPolicy, self).__init__(**kwargs)
        self.rules = kwargs.get('rules', None)
