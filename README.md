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
terraform apply\
terraform destroy
 
# Implementation Notes

| Component | Description |
| --- | --- |
| Files | Related resources are grouped together in generated files, but individual files can be generated if desired by using -i command argument. |
| Files | Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes. |
| Sheets | Sheets can be copied using a sheet name of the form basename-yourname where basename is the original sheet name (e.g. instances-group1). |
| Sheets | Asterisk in column name denotes a required field, column names are generally same as resource arguments with some changes for spreadsheet clarity, uniqueness, etc, and columns are subject to change as arguments are added or deprecated but there is no upgrade between sheet versions. |
| Sheets | A colon in a value separates multiple arguments, a comma separates list elements, and a semicolon separates array elements.  These are subject to change to ensure best mapping to spreadsheet.
| Floating IP | Created from FIP name on NIC or Public Gateway for ease of use.  Move FIP to another NIC or Public Gateway by removing FIP from previous location and adding FIP to new location, then rerun terraformer and rely on Terraform to handle the change.  Mapping to FIP resource: name and target are utilized, but zone and timeouts are not utilized. |
| Public Gateway | Created from Public Gateway name (form is gatewayname:fipname where fipname is optional) on subnet for ease of use.  Mapping to Public Gateway resource: name, vpc, zone, and floating_ip.address are utilized, but floating_ip.id, resource_controller_url, and timeouts are not utilized. |
| Rules | Header table is included to right of rules table for ease of use. |
| Rules | Protocols are in the form icp:type:code or tcp:port_min:port_max or udp:port_min:port_max or if protocol is not specified the protocol is automatically defined as ALL by Terraform. Valid values: type is 0 to 254, code is 0 to 255, port_min is 1 to 65535, port_max is 1 to 65535. |
| TBD | Empty columns in examples are currently disabled until testing is complete. |
| TBD | LB, VPN, ACLs, Secondary Volumes, and Secondary NICs are disabled until GA in Gen2. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.3 | 2019-11-28 | 0.19.0 | Added gateway:fip to public_gateway on subnet and added -i to command. |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0 | Gen1 added with same features as Gen2. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0 | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |
