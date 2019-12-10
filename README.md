# Terraformer for IBM Virtual Private Cloud

Automate creation of Terraform for IBM Virtual Private Cloud

![TerraformerExample](/images/terraformerexample.png)

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
 
# Implementation Notes

| Component | Description |
| --- | --- |
| Files | Resources are separated between a vpc spreadsheet (resources for a single vpc) and a shared spreadsheet (resources outside a single vpc). |
| Files | Related resources are grouped together in generated files or use -i command argument for one file per resource except security group rules, with one resource per rule, are still grouped together. |
| Files | Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes. |
| Sheets | Sheets can be copied using a sheet name of the form basename-groupname where basename is the original sheet name (e.g. instances-group1). |
| Sheets | Columns are subject to change but no upgrade between sheet versions. Sheet changes are mentioned in the release notes to allow an existing spreadsheet to be updated directly or use the changed example spreadsheet. |
| Sheets | Asterisk in column name denotes a required field, column names are generally same as resource arguments with some changes for spreadsheet clarity.
| Sheets | A colon in a value separates structure arguments, a comma separates list elements, and a semicolon separates array elements.  This format is subject to change to ensure best spreadsheet utilization.
| Floating IP | Created from FIP name on NIC or Public Gateway for ease of use.  Move FIP to another NIC or Public Gateway by removing FIP from previous location and adding FIP to new location, then rerun terraformer and rely on Terraform to handle the change.  Mapping to FIP resource: name and target are utilized, but zone is not utilized, and create/delete timeouts use the Terraform default of 10 minutes. |
| Public Gateway | Created from Public Gateway name (form is gatewayname:fipname where fipname is optional) on subnet for ease of use.  Mapping to Public Gateway resource: name, vpc, zone, and floating_ip.address are utilized, but floating_ip.id and resource_controller_url are not utilized, and create/delete timeouts use the Terraform default of 60 minutes. |
| Rules | Rules sheet includes a rules table on the left since rules vary and header table on right to prevent redundancy by specifying header details once and in case additional header arguments are added to the product. |
| Rules | Protocols are in the form icp:type:code or tcp:port_min:port_max or udp:port_min:port_max or if protocol is not specified the protocol is automatically defined as ALL by Terraform. Valid values: type is 0 to 254, code is 0 to 255, port_min is 1 to 65535, port_max is 1 to 65535. |
| Resource Groups | As mentioned in terraform docs, terraform destroy only removes the terraform state information for the resource group and does not delete the resource group.
| TBD | LB, VPN, Secondary NICs, and Custom Images are not available for Gen1 or Gen2, and Network ACLs are available for Gen1 but not Gen2. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.8 | 2019-12-09 | 0.20.0+ | Combined Gen 1 and Gen 2 examples. |
| | | | Updated vpc menus to improve image profiles readability.  |
| 0.0.0.0.7 | 2019-12-08 | 0.20.0+ | Added vpc volumes sheet.  |
| 0.0.0.0.6 | 2019-12-08 | 0.20.0+ | Added shared acls sheet.  |
| 0.0.0.0.5 | 2019-12-07 | 0.20.0+ | Added shared resourcegroups sheet. |
| | | | Updated vpc instances to replace boot_volume with boot_volume_name and boot_volume_encryption. |
| 0.0.0.0.4 | 2019-12-03 | 0.19.0+ | Fixed subnet/instance timeouts. |
| | | | Added -p to command to include prefixes on names for shared accounts. |
| 0.0.0.0.3 | 2019-11-28 | 0.19.0+ | Updated vpc subnets to allow gateway:fip on public_gateway.
| | | | Added -i to command to generate individual files excluding security group. |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0+ | Gen 1 in sync with Gen 2 features. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0+ | Gen 2, no LB or VPN or ACLs or secondary volumes/NICs or custom images. |
