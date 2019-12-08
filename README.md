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
| Files | Related resources are grouped together in generated files, but individual files can be generated if desired by using -i command argument. |
| Files | Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes. |
| Sheets | Sheets can be copied using a sheet name of the form basename-groupname where basename is the original sheet name (e.g. instances-group1). |
| Sheets | Columns are subject to change but no upgrade between sheet versions. The sheet changes section below is intended to allow an existing spreadsheet to be updated directly, or use the changed example spreadsheet. |
| Sheets | Asterisk in column name denotes a required field, column names are generally same as resource arguments with some changes for spreadsheet clarity.
| Sheets | A colon in a value separates structure arguments, a comma separates list elements, and a semicolon separates array elements.  This format is subject to change to ensure best spreadsheet utilization.
| Floating IP | Created from FIP name on NIC or Public Gateway for ease of use.  Move FIP to another NIC or Public Gateway by removing FIP from previous location and adding FIP to new location, then rerun terraformer and rely on Terraform to handle the change.  Mapping to FIP resource: name and target are utilized, but zone is not utilized, and create/delete timeouts use the Terraform default of 10 minutes. |
| Public Gateway | Created from Public Gateway name (form is gatewayname:fipname where fipname is optional) on subnet for ease of use.  Mapping to Public Gateway resource: name, vpc, zone, and floating_ip.address are utilized, but floating_ip.id and resource_controller_url are not utilized, and create/delete timeouts use the Terraform default of 60 minutes. |
| Rules | Rules sheet includes a rules table on the left since rules vary and header table on right to prevent redundancy by specifying header details once and in case additional header arguments are added to the product. |
| Rules | Protocols are in the form icp:type:code or tcp:port_min:port_max or udp:port_min:port_max or if protocol is not specified the protocol is automatically defined as ALL by Terraform. Valid values: type is 0 to 254, code is 0 to 255, port_min is 1 to 65535, port_max is 1 to 65535. |
| TBD | LB, VPN, ACLs, Secondary Volumes, and Secondary NICs are disabled until GA in Gen2. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.5 | 2019-12-07 | 0.20.0+ | Renamed regional to shared, refer to sheet change 0001.  |
| 0.0.0.0.4 | 2019-12-03 | 0.19.0+ | Fixed subnet/instance timeouts, added -p to command. |
| 0.0.0.0.3 | 2019-11-28 | 0.19.0+ | Added gateway:fip to public_gateway on subnet, added -i to command. |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0+ | Gen1 added with same features as Gen2. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0+ | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |

# Sheet Changes

| Number | Version | Sheet | Description |
| --- | --- | --- | --- |
| 0001 | 0.0.0.0.5 | resourcegroups | Added sheet to shared. |
| | | instances | Renamed column boot_volume to boot_volume_name and added column boot_volume_encryption. |
