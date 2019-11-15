# Terraformer for IBM Virtual Private Cloud

Generates Terraform from spreadsheets for IBM Virtual Private Cloud:

![TerraformerExample](/images/terraformerexample.png)

# Usage Steps

1. Export API credential tokens as environment variables:\
export IC_API_KEY="IBM Cloud API Key"\
export IAAS_CLASSIC_API_KEY="IBM Cloud Classic Infrastructure API Key"\
export IAAS_CLASSIC_USERNAME="IBM Cloud Classic Infrastructure Username"

2. Execute terraformer to output directory:\
terraformer -h\
terraformer -g 1 -r Dallas global.xlsx\
terraformer -g 1 -r Dallas vpc.xlsx

3. Execute terraform in output directory:\
terraform fmt\
terraform init\
terraform plan\
terraform apply
 
# Implementation Notes

1. Provided for Gen2 only as-is test stage for feedback while continuing testing and improving.
2. Sheet format and columns are subject to change and no upgrade from previous sheets to changed sheets but changes will be documented.
3. Rerunning after modifying a spreadsheet will regenerate and rely on the existing Terraform state to determine changes.
4. Related resources are grouped together in generated files.
5. Asterisk in column header is used to denote a required field.
6. Some columns are set to not generate until testing is complete.
7. Not implemented:  LB, VPN, ACLs, Secondary NICs

# Release Notes

0.0.0.0.1TEST - Initial test release with limited functionality and no LB, VPN, ACLs, or secondary NICs.
