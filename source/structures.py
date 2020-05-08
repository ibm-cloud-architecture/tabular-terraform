# Terraformer for IBM Virtual Private Cloud
#
# Copyright IBM Corporation 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Variables

varsyntax = 'variable %s_%s { default = "%s" }\n'
varsyntax2 = 'variable %s { default = "%s" }\n'
refsyntax = 'var.%s_%s'

# User options

useroptions = {
'datapath': 'data',
'datavars': False,
'generation': '2',
'genpath': 'resources',
'individual': False,
'prepend': '',
'propext': 'xlsx',
'propfile': '',
'propname': '*',
'puml': False,
'region': 'Dallas'
}

# Resource names

providerresource = 'provider'
varresource = 'variables'
rgresource = 'ibm_resource_group'
vpcresource = 'ibm_is_vpc'
vpcaddressresource = 'ibm_is_vpc_address_prefix'
vpcrouteresource = 'ibm_is_vpc_route'
subnetresource = 'ibm_is_subnet'
instanceresource = 'ibm_is_instance'
secondarynicresource = 'ibm_is_instance_nic'
volumeresource = 'ibm_is_volume'
fipresource = 'ibm_is_floating_ip'
pubgatewayresource = 'ibm_is_public_gateway'
vpnresource = 'ibm_is_vpn_gateway'
vpnconnectresource = 'ibm_is_vpn_gateway_connection'
ikepolicyresource = 'ibm_is_ike_policy'
ipsecpolicyresource = 'ibm_is_ipsec_policy'
imageresource = 'ibm_is_image'
sshkeyresource = 'ibm_is_ssh_key'
lbresource = 'ibm_is_lb'
lbpoolresource = 'ibm_is_lb_pool'
lbmemberresource = 'ibm_is_lb_pool_member'
lblistenerresource = 'ibm_is_lb_listener'
lbpolicyresource = 'ibm_is_lb_listener_policy'
lbruleresource = 'ibm_is_lb_listener_policy_rule'
aclresource = 'ibm_is_network_acl'
aclruleresource = 'ibm_is_network_acl'
sgresource = 'ibm_is_security_group'
sgruleresource = 'ibm_is_security_group_rule'
sgnicresource = 'ibm_is_security_group_network_interface_attachment'

resourceheader = 'resource "%s" "%s"'

# Resource file names

varsfilename = 'variables_%s.tf'
providerfile = providerresource + '_%s.tf'
varfile = varresource + '.tf'
rgfile = rgresource + '_%s.tf'
vpcfile = vpcresource + '_%s.tf'
vpcaddressfile = vpcaddressresource + '_%s.tf'
vpcroutefile = vpcrouteresource + '_%s.tf'
subnetfile = subnetresource + '_%s.tf'
instancefile = instanceresource + '_%s.tf'
volumefile = volumeresource + '_%s.tf'
fipfile = fipresource + '_%s.tf'
pubgatewayfile = pubgatewayresource + '_%s.tf'
vpnfile = vpnresource + '_%s.tf'
vpnconnectfile = vpnconnectresource + '_%s.tf'
ikepolicyfile = ikepolicyresource + '_%s.tf'
ipsecpolicyfile = ipsecpolicyresource + '_%s.tf'
imagefile = imageresource + '_%s.tf'
sshkeyfile = sshkeyresource + '_%s.tf'
lbfile = lbresource + '_%s.tf'
lbpoolfile = lbpoolresource + '_%s.tf'
lbmemberfile = lbmemberresource + '_%s.tf'
lblistenerfile = lblistenerresource + '_%s.tf'
lbpolicyfile = lbpolicyresource + '_%s.tf'
lbrulefile = lbruleresource + '_%s.tf'
aclfile = aclresource + '_%s.tf'
aclrulefile = aclruleresource + '_%s.tf'
sgfile = sgresource + '_%s.tf'
sgrulefile = sgruleresource + '_%s.tf'
sgnicfile = sgnicresource + '_%s.tf'

fipstructure = 'floating_ip'
primarynicstructure = 'primary_network_interface'
networkinterfacesstructure = 'network_interfaces'
timeoutstructure = 'timeouts'
icmpstructure = 'icmp'
tcpstructure = 'tcp'
udpstructure = 'udp'

# Field details

providerfields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', False),
'ibmcloud_api_key':
   ('ibmcloud_api_key', 'string', 'optional', 'value', '', False),
'ibmcloud_timeout':
   ('ibmcloud_timeout', 'string', 'optional', 'value', '', False),
'iaas_classic_username':
   ('iaas_classic_username', 'string', 'optional', 'value', '', False),
'iaas_classic_api_key':
   ('iaas_classic_api_key', 'string', 'optional', 'value', '', False),
'iaas_classic_endpoint_url':
   ('iaas_classic_endpoint_url', 'string', 'optional', 'value', '', False),
'iaas_classic_timeout':
   ('iaas_classic_timeout', 'string', 'optional', 'value', '', False),
'region':
   ('region', 'string', 'optional', 'region', '', False),
'resource_group':
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', False),
'max_retries':
   ('max_retries', 'string', 'optional', 'value', '', False),
'function_namespace':
   ('function_namespace', 'string', 'optional', 'value', '', False),
'generation':
   ('generation', 'string', 'optional', 'value', '', False)
}

varfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'value':
   ('value', 'string', 'required', 'value', '', True),
'type':
   ('type', 'string', 'optional', 'value', '', True),
'description':
   ('description', 'string', 'optional', 'value', '', True)
}

rgfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'tags':
   ('tags', 'string array', 'optional', 'value', '', False)
}

vpcfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'address_prefix_management':
   ('address_prefix_management', 'string', 'optional', 'value', '', False),
'classic_access':
   ('classic_access', 'string', 'optional', 'value', '', False),  # bool
'resource_group':
   ('resource_group', 'string', 'optional', 'id', rgresource, True),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False)
}

vpcaddressfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'vpc': 
   ('vpc', 'string', 'required', 'id', vpcresource, True),
'zone':
   ('zone', 'string', 'required', 'zone', '', False),
'cidr':
   ('cidr', 'string', 'required', 'value', '', False)
} 

vpcroutefields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'vpc': 
   ('vpc', 'string', 'required', 'id', vpcresource, True),
'zone':
   ('zone', 'string', 'required', 'zone', '', False),
'destination':
   ('destination', 'string', 'required', 'value', '', False),
'next_hop':
   ('next_hop', 'string', 'required', 'value', '', False)
} 

subnetfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'vpc': 
   ('vpc', 'string', 'required', 'id', vpcresource, True),
'zone': 
   ('zone', 'string', 'required', 'zone', '', False),
'ipv4_cidr_block': 
   ('ipv4_cidr_block', 'string', 'optional', 'value', '', False),
'total_ipv4_address_count': 
   ('total_ipv4_address_count', 'string', 'optional', 'value', '', False),
'ip_version': 
   ('ip_version', 'string', 'optional', 'value', '', False),
'network_acl': 
   ('network_acl', 'string', 'optional', 'id', aclresource, True),
'public_gateway': 
   ('public_gateway', 'string', 'optional', 'id', pubgatewayresource, True),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'create_timeout': 
   ('create', 'string', 'optional', 'timeout', '', False),
'update_timeout': 
   ('update', 'string', 'optional', 'timeout', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'timeout', '', False)
}

instancefields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'vpc': 
   ('vpc', 'string' , 'required', 'id', vpcresource, True),
'zone': 
   ('zone', 'string', 'required', 'zone', '', False),
'profile': 
   ('profile', 'string', 'required', 'imageprofile', '', False),
'image': # @revisit pointing to image
   ('image', 'string', 'optional', 'image', '', False),
'boot_volume': 
   ('name', 'string', 'optional', 'nogen', '', False),
'keys': 
   ('keys', 'string array', 'required', 'id', sshkeyresource, True),
'volumes': 
   ('volumes', 'string array', 'optional', 'id', volumeresource, True),
'user_data': 
   ('user_data', 'string', 'optional', 'value', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False),
'primary_network_interface': 
   ('name', 'string', 'required', 'primarynic', '', True),
'network_interfaces': 
   ('network_interfaces', 'string', 'optional', 'networkinterfaces', '', True),
'create_timeout': 
   ('create', 'string', 'optional', 'timeout', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'timeout', '', False)
}

networkinterfacefields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'instance': 
  ('instance', 'string', 'required', 'nogen', '', True),
'interface_type': 
  ('interface_type', 'string', 'required', 'nogen', '', False),
'subnet': 
   ('subnet', 'string', 'required', 'id', subnetresource, True),
'security_groups': 
   ('security_groups', 'string array', 'optional', 'id', sgresource, True),
'floating_ip':
   ('fip', 'string', 'optional', 'nogen', '', True)
}

volumefields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'instance': 
  ('instance', 'string', 'required', 'nogen', '', True),
'attachment_type': 
  ('attachment_type', 'string', 'required', 'nogen', '', False),
'profile': 
   ('profile', 'string', 'required', 'volumeprofile', '', False),
'zone': 
   ('zone', 'string', 'required', 'zone', '', False),
'iops': 
   ('iops', 'string', 'optional', 'value', '', False),  # int 100-20000
'capacity': 
   ('capacity', 'string', 'optional', 'value', '', False),  # int 10-2000
'encryption_key': 
   ('encryption_key', 'string', 'optional', 'value', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'resource_controller_url': 
   ('resource_controller_url', 'string', 'optional', 'value', '', False),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

fipfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'subnet': # Subnet name is only used for adding fip to subnet file. 
  ('subnet', 'string', 'required', 'nogen', '', True),
'target': # @revisit handle secondary nics 
  ('target', 'string', 'optional', 'primary_network_interface.0.id', instanceresource, True),
'zone': 
   ('zone', 'string', 'optional', 'zone', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

pubgatewayfields = {
'name': 
   ('name', 'string', 'optional', 'value', '', True), # @revisit required
'subnet': # Subnet name is only used for adding pubgateway to subnet file. 
   ('subnet', 'string', 'required', 'nogen', '', True),
'vpc': 
   ('vpc', 'string', 'required', 'id', vpcresource, True),
'zone': 
   ('zone', 'string', 'required', 'zone', '', False),
'floating_ip_id': 
   ('id', 'string', 'optional', 'id', fipresource, True),
'floating_ip_address': 
   ('address', 'string', 'optional', 'value', '', False),
'resource_controller_url': 
   ('resource_controller_url', 'string', 'optional', 'value', '', False),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

vpngatewayfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'subnet': 
   ('subnet', 'string', 'required', 'id', subnetresource, True),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True)
}

vpnconnectionfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'vpn_gateway': 
   ('vpn_gateway', 'string' , 'optional', 'id', vpnresource, True),
'peer_address': 
   ('peer_address', 'string', 'required', 'public_ip_address', vpnresource, True),
'preshared_key': 
   ('preshared_key', 'string', 'required', 'value', '', False),
'local_cidrs': 
   ('local_cidrs', 'string array', 'optional', 'ipv4_cidr_block', subnetresource, True),
'peer_cidrs': 
   ('peer_cidrs', 'string array', 'optional', 'ipv4_cidr_block', subnetresource, True),
'admin_state_up': 
   ('admin_state_up', 'string', 'optional', 'value', '', False), # bool
'dead_peer_action': 
   ('action', 'string', 'optional', 'value', '', False),
'dead_peer_interval': 
   ('interval', 'string', 'optional', 'value', '', False), # int
'dead_peer_timeout': 
   ('timeout', 'string', 'optional', 'value', '', False), # int
'ike_policy': 
   ('ike_policy', 'string', 'optional', 'id', ikepolicyresource, True),
'ipsec_policy': 
   ('ipsec_policy', 'string', 'optional', 'id', ipsecpolicyresource, True),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

ikepolicyfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'authentication_algorithm': 
   ('authentication_algorithm', 'string' , 'required', 'value', '', False),
'encryption_algorithm': 
   ('encryption_algorithm', 'string' , 'required', 'value', '', False),
'dh_group': 
   ('dh_group', 'string', 'required', 'value', '', False), # int
'ike_version': 
   ('ike_version', 'string', 'optional', 'value', '', False), # int
'key_lifetime': 
   ('key_lifetime', 'string', 'optional', 'value', '', False), # int
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True)
}

ipsecpolicyfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'authentication_algorithm': 
   ('authentication_algorithm', 'string' , 'required', 'value', '', False),
'encryption_algorithm': 
   ('encryption_algorithm', 'string' , 'required', 'value', '', False),
'pfs': 
   ('pfs', 'string', 'required', 'value', '', False),
'key_lifetime': 
   ('key_lifetime', 'string', 'optional', 'value', '', False), # int
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True)
}

imagefields = {
'name': 
   ('name', 'string', 'required', 'value', '', False),
'href': 
   ('href', 'string', 'required', 'value', '', False),
'operating_system': 
   ('operating_system', 'string', 'required', 'value', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False)
}

sshkeyfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'public_key': 
   ('public_key', 'string', 'required', 'file', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False)
} 

lbfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'subnets': 
   ('subnets', 'string array' , 'required', 'id', subnetresource, True),
'type': 
   ('type', 'string' , 'optional', 'value', '', False),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True),
'tags':
   ('tags', 'string array', 'optional', 'value', '', False),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

lbpoolfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'lb': 
   ('lb', 'string' , 'required', 'id', lbresource, True),
'algorithm': 
   ('algorithm', 'string' , 'required', 'value', '', False),
'protocol': 
   ('protocol', 'string', 'required', 'value', '', False),
'health_delay': 
   ('health_delay', 'string', 'required', 'value', '', False), # int
'health_retries': 
   ('health_retries', 'string', 'required', 'value', '', False), # int
'health_timeout': 
   ('health_timeout', 'string', 'required', 'value', '', False), # int
'health_type': 
   ('health_type', 'string', 'required', 'value', '', False),
'health_monitor_url': 
   ('health_monitor_url', 'string', 'optional', 'value', '', False),
'health_monitor_port': 
   ('health_monitor_port', 'string', 'optional', 'value', '', False),
'session_persistence_type':
   ('session_persistency_type', 'string', 'optional', 'value', '', False),
'session_persistence_cookie_name': 
   ('session_persistence_cookie_name', 'string', 'optional', 'value', '', False),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'update_timeout': 
   ('update', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

lbmemberfields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', True),
'pool': 
   ('pool', 'string', 'required', 'id', lbpoolresource, True),
'lb': 
   ('lb', 'string', 'required', 'id', lbresource, True),
'port': 
   ('port', 'string', 'required', 'value', '', False), # int
'target_address': 
   ('target_address', 'string', 'required', 'primary_network_interface.0.primary_ipv4_address', instanceresource, True),
'weight': 
   ('weight', 'string', 'optional', 'value', '', False), # int
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'update_timeout': 
   ('update', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

lblistenerfields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', True),
'lb': 
   ('lb', 'string', 'required', 'id', lbresource, True),
'port': 
   ('port', 'string', 'required', 'value', '', False), # int
'protocol': 
   ('protocol', 'string', 'required', 'value', '', False),
'default_pool': 
   ('default_pool', 'string', 'optional', 'id', lbpoolresource, False),
'certificate_instance': 
   ('certificate_instance', 'string', 'optional', 'value', '', False),
'connection_limit': 
   ('connection_limit', 'string', 'optional', 'value', '', False), # int
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'update_timeout': 
   ('update', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

lbpolicyfields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', True),
'lb': 
   ('lb', 'string', 'required', 'id', lbresource, True),
'listener': 
   ('listener', 'string', 'required', 'id', lblistenerresource, True),
'action': 
   ('action', 'string', 'required', 'value', '', True),
'priority': 
   ('priority', 'string', 'required', 'value', '', True),
'target_id': 
   ('target_id', 'string', 'optional', 'value', '', False),
'target_http_status_code': 
   ('target_http_status_code', 'string', 'optional', 'value', '', False),
'target_url': 
   ('target_url', 'string', 'optional', 'value', '', False)
}

lbrulefields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', True),
'lb': 
   ('lb', 'string', 'required', 'id', lbresource, True),
'listener': 
   ('listener', 'string', 'required', 'id', lblistenerresource, True),
'policy': 
   ('policy', 'string', 'required', 'id', lbpolicyresource, True),
'condition': 
   ('condition', 'string', 'required', 'value', '', True),
'type': 
   ('type', 'string', 'required', 'value', '', True),
'value': 
   ('value', 'string', 'optional', 'value', '', False),
'field': 
   ('field', 'string', 'optional', 'value', '', False),
'create_timeout': 
   ('create', 'string', 'optional', 'nogen', '', False),
'update_timeout': 
   ('update', 'string', 'optional', 'nogen', '', False),
'delete_timeout': 
   ('delete', 'string', 'optional', 'nogen', '', False)
}

aclheaderfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'vpc': 
   # @revisit remove gen2
   ('vpc', 'string', 'gen2required', 'id', vpcresource, True),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True)
} 

aclrulefields = {
'name': 
   ('name', 'string', 'required', 'value', '', True),
'acl':
   ('acl', 'string', 'required', 'nogen', '', True),
'action': 
   ('action', 'string', 'required', 'value', '', False),
'source': 
   ('source', 'string', 'required', 'value', '', False),
'destination': 
   ('destination', 'string', 'required', 'value', '', False),
'direction': 
   ('direction', 'string', 'required', 'value', '', False),
'protocol': 
   ('protocol', 'string', 'optional', 'protocol', '', False),
'icmp_code': 
   ('icmp_code', 'string', 'optional', 'protocolvalue', '', False),
'icmp_type': 
   ('icmp_type', 'string', 'optional', 'protocolvalue', '', False),
'port_min': 
   ('port_min', 'string', 'optional', 'protocolvalue', '', False),
'port_max': 
   ('port_max', 'string', 'optional', 'protocolvalue', '', False),
'source_port_min': 
   ('source_port_min', 'string', 'optional', 'protocolvalue', '', False),
'source_port_max': 
   ('source_port_max', 'string', 'optional', 'protocolvalue', '', False)
}

sgheaderfields = {
'name': 
   ('name', 'string', 'required', 'value', '', True), 
'vpc': 
   ('vpc', 'string', 'required', 'id', vpcresource, True),
'resource_group': 
   ('resource_group', 'string', 'optional', 'id', 'resource_group_resource', True)
} 

sgrulefields = {
'name': 
   ('name', 'string', 'required', 'nogen', '', True),
'group':
   ('group', 'string', 'required', 'id', sgresource, True), 
'direction': 
   ('direction', 'string', 'required', 'value', '', False),
'remote': # @revisit remote can be id or value 
   ('remote', 'string', 'required', 'value', '', False),
'ip_version': 
   ('ip_version', 'string', 'optional', 'value', '', False),
'protocol': 
   ('protocol', 'string', 'optional', 'protocol', '', False),
'icmp_code': 
   ('icmp_code', 'string', 'optional', 'protocolvalue', '', False),
'icmp_type': 
   ('icmp_type', 'string', 'optional', 'protocolvalue', '', False),
'port_min': 
   ('port_min', 'string', 'optional', 'protocolvalue', '', False),
'port_max': 
   ('port_max', 'string', 'optional', 'protocolvalue', '', False)
}

sgnicfields = {
'security_group': 
   ('security_group', 'string', 'required', 'id', sgresource, True),
'network_interface':
   ('network_interface', 'string', 'required', 'id', instanceresource, True)
}

# Dictionaries

providerdictionary = {
'resource':providerresource, 
'file':providerfile, 
'fields':providerfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

rgdictionary = {
'resource':rgresource, 
'file':rgfile, 
'fields':rgfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

vardictionary = {
'resource':varresource, 
'file':varfile, 
'fields':varfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

vpcdictionary = {
'resource':vpcresource, 
'file':vpcfile, 
'fields':vpcfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

vpcaddressdictionary = {
'resource':vpcaddressresource, 
'file':vpcaddressfile, 
'fields':vpcaddressfields, 
'header':{},
'structures':{},
'parent':'vpc', 
'parentfile':vpcfile 
}

vpcroutedictionary = {
'resource':vpcrouteresource, 
'file':vpcroutefile, 
'fields':vpcroutefields, 
'header':{},
'structures':{},
'parent':'vpc', 
'parentfile':vpcfile 
}

subnetdictionary = {
'resource':subnetresource, 
'file':subnetfile, 
'fields':subnetfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'', 
'parentfile':'' 
}

instancedictionary = {
'resource':instanceresource, 
'file':instancefile, 
'fields':instancefields, 
'header':{},
'structures':{'nic':primarynicstructure, 'timeout':timeoutstructure},
'parent':'primary_network_interface:networkinterfaces:subnet', 
'parentfile':subnetfile 
}

networkinterfacedictionary = {
'resource':instanceresource, 
'file':instancefile, 
'fields':networkinterfacefields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

volumedictionary = {
'resource':volumeresource, 
'file':volumefile, 
'fields':volumefields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'', 
'parentfile':'' 
}

fipdictionary = {
'resource':fipresource, 
'file':fipfile, 
'fields':fipfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'subnet', 
'parentfile':subnetfile 
}

pubgatewaydictionary = {
'resource':pubgatewayresource, 
'file':pubgatewayfile, 
'fields':pubgatewayfields, 
'header':{},
'structures':{'fip':fipstructure, 'timeout':timeoutstructure},
'parent':'subnet', 
'parentfile':subnetfile 
}

vpngatewaydictionary = {
'resource':vpnresource, 
'file':vpnfile, 
'fields':vpngatewayfields,
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

vpnconnectiondictionary = {
'resource':vpnconnectresource, 
'file':vpnconnectfile, 
'fields':vpnconnectionfields, 
'header':vpngatewaydictionary,
'structures':{'timeout':timeoutstructure},
'parent':'vpn_gateway', 
'parentfile':vpnfile 
}

ikepolicydictionary = {
'resource':ikepolicyresource, 
'file':ikepolicyfile, 
'fields':ikepolicyfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

ipsecpolicydictionary = {
'resource':ipsecpolicyresource, 
'file':ipsecpolicyfile, 
'fields':ipsecpolicyfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

imagedictionary = {
'resource':imageresource, 
'file':imagefile, 
'fields':imagefields,
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

sshkeydictionary = {
'resource':sshkeyresource, 
'file':sshkeyfile, 
'fields':sshkeyfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

lbdictionary = {
'resource':lbresource, 
'file':lbfile, 
'fields':lbfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'', 
'parentfile':'' 
}

lbpooldictionary = {
'resource':lbpoolresource, 
'file':lbpoolfile, 
'fields':lbpoolfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'lb', 
'parentfile':lbfile 
}

lbmemberdictionary = {
'resource':lbmemberresource, 
'file':lbmemberfile, 
'fields':lbmemberfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'lb', 
'parentfile':lbfile 
}

lblistenerdictionary = {
'resource':lblistenerresource, 
'file':lblistenerfile, 
'fields':lblistenerfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'lb', 
'parentfile':lbfile 
}

lbpolicydictionary = {
'resource':lbpolicyresource, 
'file':lbpolicyfile, 
'fields':lbpolicyfields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'lb', 
'parentfile':lbfile 
}

lbruledictionary = {
'resource':lbruleresource, 
'file':lbrulefile, 
'fields':lbrulefields, 
'header':{},
'structures':{'timeout':timeoutstructure},
'parent':'lb', 
'parentfile':lbfile 
}

aclheaderdictionary = {
'resource':aclresource, 
'file':aclfile, 
'fields':aclheaderfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':''
}

aclruledictionary = {
'resource':aclruleresource, 
'file':aclfile,
'fields':aclrulefields, 
'header':aclheaderdictionary,
'structures':{},
'parent':'acl',
'parentfile':aclfile 
}

sgheaderdictionary = {
'resource':sgresource, 
'file':sgfile, 
'fields':sgheaderfields, 
'header':{},
'structures':{},
'parent':'', 
'parentfile':'' 
}

sgruledictionary = {
'resource':sgruleresource, 
'file':sgrulefile, 
'fields':sgrulefields, 
'header':sgheaderdictionary,
'structures':{},
'parent':'group',
'parentfile':sgfile
}

sgnicdictionary = {
'resource':sgnicresource, 
'file':sgnicfile, 
'fields':sgnicfields, 
'header':{},
'structures':{},
'structures':{},
'parent':'', 
'parentfile':sgfile 
}

# Top-level resource details dictionary

alldetails = {
'provider':providerdictionary, 
'variables':vardictionary, 
'resourcegroups':rgdictionary, 
'vpcheaders':vpcdictionary, 
'vpcaddresses':vpcaddressdictionary, 
'vpcroutes':vpcroutedictionary, 
'subnets':subnetdictionary, 
'instances':instancedictionary, 
'networkinterfaces':networkinterfacedictionary, 
'volumes':volumedictionary, 
'fips':fipdictionary,
'publicgateways':pubgatewaydictionary, 
'vpngateways':vpngatewaydictionary, 
'vpnconnections':vpnconnectiondictionary, 
'ikepolicies':ikepolicydictionary, 
'ipsecpolicies':ipsecpolicydictionary, 
'images':imagedictionary, 
'sshkeys':sshkeydictionary, 
'loadbalancers':lbdictionary, 
'lbpools':lbpooldictionary, 
'lbmembers':lbmemberdictionary, 
'lblisteners':lblistenerdictionary, 
'lbpolicies':lbpolicydictionary, 
'lbrules':lbruledictionary, 
'aclheaders':aclheaderdictionary,
'aclrules':aclruledictionary,
'sgheaders':sgheaderdictionary,
'sgrules':sgruledictionary
}
