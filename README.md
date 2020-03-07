# Terraformer for IBM Virtual Private Cloud

Terraformer automates creation of Terraform for IBM Virtual Private Cloud.

For new Terraform users, Terraformer helps to get on the Terraform bandwagon to learn Terraform without focusing on the Terraform syntax. 

For experienced Terraform users, Terraformer helps to expedite the implementation of Terraform, or Terraformer can used to expedite specific parts of a Terraform implementation such as rules for ACLs and Security Groups.

Terraformer 1.2.3.1 ([Terraformer Release Notes](releases.md))\
IBM Cloud Terraform Provider 1.2.3 ([Provider Release Notes](https://github.com/IBM-Cloud/terraform-provider-ibm/releases))\
Python 3.8.2 ([Python Release Notes](https://www.python.org/downloads/release/python-382/))

To create diagrams for IBM Virtual Private Cloud refer to [IBM Cloud Stencils](https://github.com/ibm-cloud-architecture/ibm-cloud-stencils).

# Overview

1. Terraformer is provided with no formal support and the format is subject to change.
2. Report problems informally by opening a GitHub issue.
3. All fields, custom images, secondary NICs, and Power need further testing.
4. Additional fields in floatingips and publicgateways sheets are not yet supported.
5. Considering adding resource-specific fields such as count.
6. Considering migrating sheets when format changes are required.

# Example

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample12](/images/terraformeroutputexample12.png)

# Usage

1. Export API credential token as an environment variable:\
export IC_API_KEY="IBM Cloud API Key"

2. Install Python 3.8.2 on Mac or Windows from https://www.python.org/ with following libraries:
- pip install numpy
- pip install pandas
- pip install xlrd

3. Install terraformer:
- Copy mac/terraformer executable to Mac or windows/terraformer.exe to Windows.
- Copy examples/*.xlsx to Mac or Windows and customize as desired.
- Run terraformer on the examples as described below.

4. Execute terraformer:
- *Display help:*\
terraformer -h
- *Display version:*\
terraformer --version
- *Use Gen2, gen2output directory, add prefix, Dallas region:*\
terraformer -o gen2output -p prefix -r Dallas access.xlsx\
terraformer -o gen2output -p prefix -r Dallas lb.xlsx\
terraformer -o gen2output -p prefix -r Dallas vpc.xlsx
- *Use Gen1, gen1output directory, add prefix, Dallas region:*\
terraformer -g 1 -o gen1output -p prefix -r Dallas access.xlsx\
terraformer -g 1 -o gen1output -p prefix -r Dallas lb.xlsx\
terraformer -g 1 -o gen1output -p prefix -r Dallas vpc.xlsx

5. Execute terraform in specified output directory:\
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

# Notes

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
| | Use floatingips sheet to set additional arguments - not currently implemented. |
| Images | Profile names are Gen 1 or Gen 2 style - Gen 2 names are converted to Gen 1 names. |
| Public Gateway | Created from subnet public_gateway (e.g. gatewayname:optionalfipname). |  
| | Use publicgateways sheet to set additional arguments - not currently implemented. |
| Regions | Names are UI style or internal name (e.g. Dallas or us-south). |
| Resource Groups | Terraform destroy only removes state information but does not delete resource group.
| Volumes | Profile names are general-purpose, 5iops-tier, 10iops-tier, or custom. |
| | Only name and encryption are valid for boot volumes. |
| Zones | Names are UI style or internal name (e.g. Dallas 1 or us-south-1). |
