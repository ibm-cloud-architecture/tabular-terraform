# Terraformer for IBM Virtual Private Cloud

Automate creation of Terraform for IBM Virtual Private Cloud

![TerraformerExample](/images/terraformerexample.png)

# Usage Steps

1. Export API credential tokens as environment variables:\
export IC_API_KEY="IBM Cloud API Key"\
export IAAS_CLASSIC_API_KEY="IBM Cloud Classic Infrastructure API Key"\
export IAAS_CLASSIC_USERNAME="IBM Cloud Classic Infrastructure Username"

2. Execute terraformer to output directory:\
terraformer -h\
terraformer -g 1 -r Dallas regional.xlsx\
terraformer -g 1 -r Dallas vpc.xlsx

3. Execute terraform in output directory:\
terraform fmt\
terraform init\
terraform plan\
terraform apply
 
# Implementation Notes

| Component | Description |
| --- | --- |
| Files | Related resources are grouped together in generated files. |
| Files | Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes. |
| Format | Asterisk in column name denotes a required field. |
| Format | Column names are generally same as resource arguments with some changes for spreadsheet clarity, uniqueness, etc.
| Format | Columns are subject to change and no upgrade from previous sheets to changed sheets. |
| Format | Most values are a single string, a colon separates values that contain multiple arguments, a comma separates list elements, and a semicolon separates array elements.
| Format | Menus are provided where applicable for ease of use, utilizing UI names (e.g. Dallas 1) which are mapped to resource values (e.g. us-south-1).
| Floating IP | Created from FIP name on NIC or Public Gateway for ease of use.  Move FIP to another NIC or Public Gateway by removing FIP from previous location and adding FIP to new location, then rerun terraformer and rely on Terraform to handle the change.  Mapping to FIP resource: name and target are utilized, but zone and timeouts are not utilized. |
| Public Gateway | Created from Public Gateway name (form is gatewayname:fipname where fipname is optional) on subnet for ease of use.  Mapping to Public Gateway resource: name, vpc, zone, and floating_ip.id are utilized, but floating_ip.address, resource_controller_url, and timeouts are not utilized. |
| Rules | Header table is included to right of rules table for ease of use. |
| Rules | Protocols are in the form icp:type:code or tcp:port_min:port_max or udp:port_min:port_max or if protocol is not specified the protocol is defined as ALL. Valid values: type is 0 to 254, code is 0 to 255, port_min is 1 to 65535, port_max is 1 to 65535. |
| TBD | Empty columns in examples are currently disabled until testing is complete. |
| TBD | LB, VPN, ACLs, Secondary Volumes, and Secondary NICs are disabled until GA in Gen2. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0 | Gen1 added with same features as Gen2. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0 | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |
