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

1. Provided as-is for feedback while continuing testing and improving.
2. Sheet format and columns are subject to change and no upgrade from previous sheets to changed sheets but changes will be documented.
3. Rerunning after modifying a spreadsheet will regenerate and rely on Terraform to handle the changes.
4. Floating IPs are designated on the NIC or public gateway for simplicity.  To move the same floating IP to another NIC or public gateway just remove the floating IP name in the previous location and add the name to the new location, then rerun terraformer and rely on Terraform to handle the change.  Relating to the floating IP arguments, name and target are utilized but zone and the timeouts are not utilized.
5. Related resources are grouped together in generated files.
6. Asterisk in column header is used to denote a required field.
7. Some columns are set to not generate until testing is complete.
8. Not implemented:  LB, VPN, ACLs, secondary volumes, secondary NICs

# Release Notes

| Date | Version | Description |
| --- | --- | --- |
| 2019-11-19 | 0.0.0.0.2 | Gen1 and Gen2 with same features. |
| 2019-11-15 | 0.0.0.0.1 | Gen2 only, no LB, VPN, ACLs, secondary volumes, secondary NICs. |
