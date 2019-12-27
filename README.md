# Terraformer for IBM Virtual Private Cloud

Automate creation of Terraform for IBM Virtual Private Cloud.

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample12](/images/terraformeroutputexample12.png)
![TerraformerOutputExample11](/images/terraformeroutputexample11.png)

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
- *Use Gen1, gen1output directory, add prefix, Dallas region, Terraform v0.11:*\
terraformer -g 1 -o gen1output -p prefix -r Dallas access.xlsx\
terraformer -g 1 -o gen1output -p prefix -r Dallas vpc.xlsx
- *Use Gen2, gen2output directory, add prefix, Dallas region, Terraform v0.11:*\
terraformer -g 2 -o gen2output -p prefix -r Dallas access.xlsx\
terraformer -g 2 -o gen2output -p prefix -r Dallas vpc.xlsx
- *Use Gen2, gen2output directory, add prefix, Dallas region, Terraform v0.12:*\
terraformer -g 2 -o gen2output -p prefix -r Dallas -t 12 regional.xlsx\
terraformer -g 2 -o gen2output -p prefix -r Dallas -t 12 vpc.xlsx

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
| Files | Example spreadsheets include access, lb, and vpc. |
| | Related resources are grouped into generated files. |
| | Rerun after changes and rely on Terraform to handle changes. |
| Sheets | Use name of basename-groupname for copied sheets (e.g. instances-group1). |
| | Columns are subject to change but no upgrade between sheet versions. |
| | Asterisk in column name denotes a required field. |
| Floating IP | Created from primary_nic_floating_ip or secondary NIC or subnet public_gateway. |
| | Move FIP to another NIC/Public Gateway and rely on Terraform to handle change. |
| | Utilizes resource name and target, but zone is not utilized. |
| | Create and delete timeouts use Terraform default of 10 minutes. |
| Images | Profile names are Gen 1 or Gen 2 style - Gen 2 names are converted to Gen 1 names. |
| Public Gateway | Created from subnet public_gateway (e.g. gatewayname:optionalfipname). |  
| | Utilizes resource name, vpc, and zone, but resource_controller_url is not utilized. |
| | Create and delete timeouts use Terraform default of 60 minutes. |
| Regions | Names are UI style or internal name (e.g. Dallas or us-south). |
| Resource Groups | Terraform destroy only removes state information but does not delete resource group.
| Rules | Protocols are icp:type:code, tcp:port_min:port_max, udp:port_min:port_max, or empty. | 
| Volumes | Profile names are general-purpose, 5iops-tier, 10iops-tier, or custom. |
| | Only name and encryption are valid for boot volumes. |
| Zones | Names are UI style or internal name (e.g. Dallas 1 or us-south-1). |
| TBD | is_vpc_route, is_network_acl and is_instance/network_interfaces available for Gen1 only. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.19 | 2019-12-27 | 0.21.0/1.0.0 | Added interface_type in network_interfaces. |
| 0.0.0.0.18 | 2019-12-26 | 0.21.0/1.0.0 | Added boot_volume and removed previous boot_volume columns in instances. |
| | | | Added instance and attachment_type in volumes. |
| 0.0.0.0.17 | 2019-12-25 | 0.21.0/1.0.0 | Use any value for all fields and do all data validation in code. |
| | | | Fixed empty field check due to initial then add then delete has different empty value. |
| 0.0.0.0.16 | 2019-12-24 | 0.21.0/1.0.0 | Added vpcroutes sheet. |
| 0.0.0.0.15 | 2019-12-23 | 0.21.0/1.0.0 | Added images sheet and removed menus sheet to enable custom images. |
| 0.0.0.0.14 | 2019-12-21 | 0.21.0/1.0.0 | Added -t to command to generate Terraform v0.11 or v0.12. |
| 0.0.0.0.13 | 2019-12-21 | 0.21.0 | Added vpn spreadsheet. |
| 0.0.0.0.12 | 2019-12-20 | 0.21.0 | Added address_prefix_management to vpc. |
| | | | Added header sheet/name to rules. |
| | | | Added multiple vpc capability to vpc. |
| 0.0.0.0.11 | 2019-12-13 | 0.20.0 | Added access spreadsheet that includes ACLs and security groups sheets. |
| 0.0.0.0.10 | 2019-12-12 | 0.20.0 | Added networkinterfaces sheet to include primary and secondary. |
| | | 0.20.0 | Added primary_network_interface and removed previous primary__nic columns in instances. |
| 0.0.0.0.9 | 2019-12-10 | 0.20.0 | Added lb spreadsheet. |
| 0.0.0.0.8 | 2019-12-09 | 0.20.0 | Combined Gen 1 and Gen 2 examples. |
| | | | Updated menus to improve image profiles readability.  |
| 0.0.0.0.7 | 2019-12-08 | 0.20.0 | Added volumes sheet.  |
| 0.0.0.0.6 | 2019-12-08 | 0.20.0 | Added acls sheet.  |
| 0.0.0.0.5 | 2019-12-07 | 0.20.0 | Added resourcegroups sheet. |
| | | | Added boot_volume columns in instances. |
| 0.0.0.0.4 | 2019-12-03 | 0.19.0 | Fixed subnet/instance timeouts. |
| | | | Added -p to command to include prefixes on names for shared accounts. |
| 0.0.0.0.3 | 2019-11-28 | 0.19.0 | Updated subnets to allow gateway:fip on public_gateway.
| | | | Added -i to command to generate individual files excluding security group. |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0 | Gen 1 in sync with Gen 2 features. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0 | Gen 2, no LB or VPN or ACLs or secondary volumes/NICs or custom images. |
