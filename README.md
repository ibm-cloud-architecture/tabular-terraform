# Terraformer for IBM Virtual Private Cloud

Automate creation of Terraform for IBM Virtual Private Cloud

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample](/images/terraformeroutputexample.png)

# Usage Steps

1. Export API credential tokens as environment variables:\
export IC_API_KEY="IBM Cloud API Key"\
export IAAS_CLASSIC_API_KEY="IBM Cloud Classic Infrastructure API Key"\
export IAAS_CLASSIC_USERNAME="IBM Cloud Classic Infrastructure Username"

2. Execute terraformer:
- *Display help:*\
terraformer -h
- *Display version:*\
terraformer --version
- *Use Gen1, Dallas region, add prefix to names, one resource per file to gen1output directory:*\
terraformer -g 1 -r Dallas -p prefix -o gen1output -i regional.xlsx\
terraformer -g 1 -r Dallas -p prefix -o gen1output -i vpc.xlsx
- *Use Gen2, Dallas region, add prefix to names, group related resources in files to output directory:*\
terraformer -g 2 -r Dallas -p prefix regional.xlsx\
terraformer -g 2 -r Dallas -p prefix vpc.xlsx

3. Execute terraform in specified output directory:\
terraform fmt\
terraform init\
terraform plan\
terraform apply\
terraform destroy

# Images (IBM-provided)

| Name | Arch | Description | Other |
| --- | --- | --- | --- |
| ibm-centos7-amd64 | amd64 | CentOS 7.x - Minimal Install | |
| ibm-debian9-amd64 | amd64 | Debian GNU/Linux 9.x - Minimal Install | |
| ibm-redhat7-amd64 | amd64 | Red Hat Enterprise Linux 7.x - Minimal Install | Gen 1 only. |
| ibm-ubuntu18-amd64 | amd64 | Ubuntu Linux 18.04 LTS - Minimal Install | |
| ibm-windows2012-amd64 | amd64 | Windows Server 2012 Standard Edition | Gen 1 only. |
| ibm-windows2012r2-amd64 | amd64 | Windows Server 2012 R2 Standard Edition | Gen 1 only. |
| ibm-windows2016-amd64 | amd64 | Windows Server 2016 Standard Edition | Gen 1 only. |

# Implementation Notes

| Component | Description |
| --- | --- |
| Terraform | Supports Terraform v0.11 and v0.12 with -t command argument. |
| | Provision tested with Terraform v0.11, syntax tested with Terraform v0.12. |
| Files | Example spreadsheets include access, lb, vpc, and vpn. |
| | Related resources are grouped into generated files or use -i command argument. |
| | Rerun after changes and rely on Terraform to handle changes. |
| Sheets | Use name of basename-groupname for copied sheets (e.g. instances-group1). |
| | Columns are subject to change but no upgrade between sheet versions. |
| | Column names are generally same as resource arguments. |
| | Asterisk in column name denotes a required field. |
| Regions | Names are UI style or internal name (e.g. Dallas or us-south). |
| Zones | Names are UI style or internal name (e.g. Dallas 1 or us-south-1). |
| Image Profiles | Names are Gen 1 or Gen 2 names, or use Gen 2 only which is converted to Gen 1. |
| Volume Profiles | Names are general-purpose (3iops-tier), 5iops-tier, 10iops-tier, or custom. |
| Floating IP | Created from primary_nic_floating_ip or secondary NIC or subnet public_gateway. |
| | Move FIP to another NIC/Public Gateway and rely on Terraform to handle change. |
| | Utilizes resource name and target, but zone is not utilized. |
| | Create and delete timeouts use Terraform default of 10 minutes. |
| Public Gateway | Created from subnet public_gateway (e.g. gatewayname:optionalfipname). |  
| | Utilizes resource name, vpc, and zone, but resource_controller_url is not utilized. |
| | Create and delete timeouts use Terraform default of 60 minutes. |
| Rules | Protocols are icp:type:code, tcp:port_min:port_max, udp:port_min:port_max, or empty. | 
| Resource Groups | Terraform destroy only removes state information but does not delete resource group.
| TBD | is_vpc_route, is_security_group_network_interface_attachment are not available. |
| | is_network_acl and is_instance/network_interfaces are available for Gen1 but not Gen2. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.15 | 2019-12-23 | 0.21.0/1.0.0 | Added images sheet and removed menus sheet to enable custom images. |
| 0.0.0.0.14 | 2019-12-21 | 0.21.0/1.0.0 | Added -t to command to generate Terraform v0.11 or v0.12. |
| 0.0.0.0.13 | 2019-12-21 | 0.21.0 | Added vpn spreadsheet. |
| 0.0.0.0.12 | 2019-12-20 | 0.21.0 | Added address_prefix_management to vpc. |
| | | | Added header sheet/name to rules. |
| | | | Added multiple vpc capability to vpc. |
| 0.0.0.0.11 | 2019-12-13 | 0.20.0 | Added access spreadsheet that includes ACLs and security groups sheets. |
| 0.0.0.0.10 | 2019-12-12 | 0.20.0 | Added networkinterfaces sheet to include primary and secondary. |
| | | 0.20.0 | Updated instances to replace primary_nic columns with single primary_network_interface column. |
| 0.0.0.0.9 | 2019-12-10 | 0.20.0 | Added lb spreadsheet. |
| 0.0.0.0.8 | 2019-12-09 | 0.20.0 | Combined Gen 1 and Gen 2 examples. |
| | | | Updated menus to improve image profiles readability.  |
| 0.0.0.0.7 | 2019-12-08 | 0.20.0 | Added volumes sheet.  |
| 0.0.0.0.6 | 2019-12-08 | 0.20.0 | Added acls sheet.  |
| 0.0.0.0.5 | 2019-12-07 | 0.20.0 | Added resourcegroups sheet. |
| | | | Updated instances to replace boot_volume with optional boot_volume_name and boot_volume_encryption columns. |
| 0.0.0.0.4 | 2019-12-03 | 0.19.0 | Fixed subnet/instance timeouts. |
| | | | Added -p to command to include prefixes on names for shared accounts. |
| 0.0.0.0.3 | 2019-11-28 | 0.19.0 | Updated subnets to allow gateway:fip on public_gateway.
| | | | Added -i to command to generate individual files excluding security group. |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0 | Gen 1 in sync with Gen 2 features. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0 | Gen 2, no LB or VPN or ACLs or secondary volumes/NICs or custom images. |
