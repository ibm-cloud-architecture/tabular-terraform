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
| Sheet Format | Columns are subject to change and no upgrade from previous sheets to changed sheets. |
| Sheet Format | Asterisk in column header is used to denote a required field. |
| File Structure | Related resources are grouped together in generated files. |
| File Structure | Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes. |
| Floating IP | Created from FIP name on NIC or public gateway.  Move FIP to another NIC or public gateway by removing FIP from previous location and adding FIP to new location, then rerun terraformer and rely on Terraform to handle the change.  Mapping to FIP resource: name and target are utilized, zone and timeouts are not utilized. |
| Public Gateway | Created from Public Gateway on subnet.  Mapping to Public Gateway resource: name, vpc, zone, and floating_ip.id are utilized, floating_ip.address, resource_controller_url and timeouts are not utilized. |
| TBD | Empty columns in examples are currently disabled until testing is complete. |
| TBD | LB, VPN, ACLs, Secondary Volumes, Secondary NICs. |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 0.0.0.0.2 | 2019-11-19 | 0.19.0 | Gen1 added with same features as Gen2. |
| 0.0.0.0.1 | 2019-11-15 | 0.19.0 | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |
