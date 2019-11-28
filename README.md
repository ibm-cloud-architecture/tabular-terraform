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

1. Provided as-is for feedback.
2. Sheet format and columns are subject to change and no upgrade from previous sheets to changed sheets.
3. Related resources are grouped together in generated files.
4. Asterisk in column header is used to denote a required field.
5. Rerunning after modifying a spreadsheet will regenerate, overwriting existing generated files, and rely on Terraform to handle the changes.
6. Floating IPs are created from the floating IP name on the instance NIC or subnet public gateway for simplicity.  To move the same floating IP to another NIC or public gateway just remove the floating IP name from the previous location and add the name to the new location, then rerun terraformer and rely on Terraform to handle the change.  Relating to floating IP arguments: name and target are utilized, but zone and timeouts are not utilized.
7. Public gateways are created from the public gateway name on the subnet for simplicity.  Relating to public gateway arguments: name, vpc, zone, and floating_ip.id are utilized, but resource_controller_url and timeouts are not utilized.
8. Not implemented: Empty columns in examples are set to not generate until testing is complete.
9. Not implemented:  LB, VPN, ACLs, secondary volumes, secondary NICs.

# Release Notes

| Date | Version | Provider | Format Changes | Description |
| --- | --- | --- | --- | --- |
| 2019-11-19 | 0.0.0.0.2 | 0.19.0 | None | Gen1 added with same features as Gen2. |
| 2019-11-15 | 0.0.0.0.1 | 0.19.0 | Initial | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |
