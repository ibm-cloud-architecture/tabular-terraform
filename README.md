# Terraformer for IBM Virtual Private Cloud

## Overview

- Terraformer handles the creation of Terraform syntax leaving the user to focus on the creation of simple spreadsheet data that is used by Terraformer in creating the Terraform files.
- For new Terraform users, Terraformer helps to get on the Terraform bandwagon by using and learning Terraform without focusing on the Terraform syntax. 
- For experienced Terraform users, Terraformer helps to expedite the implementation of Terraform, or Terraformer can be used to expedite specific parts of a Terraform implementation such as the rules for ACLs and Security Groups.
- Terraformer is provided with no formal support but problems can be reported by opening a GitHub issue.
- Spreadsheet format is subject to change but a future consideration is to migrate sheets when format changes.

[Terraformer Example](/example/example.md)

[IBM Cloud Stencils](https://github.com/ibm-cloud-architecture/ibm-cloud-stencils).

## Requirements

- IBM Cloud Terraform Provider v1.2.3 ([Provider Release Notes](https://github.com/IBM-Cloud/terraform-provider-ibm/releases))
- Terraform v0.12.23 ([Terraform Release Notes](https://www.terraform.io/downloads.html))
- Python v3.8.2 ([Python Release Notes](https://www.python.org/downloads/release/python-382/)) with libraries numpy, pandas, xlrd

## Installation

1. [Download the latest Terraformer.](/releases/releases.md)
2. Unzip the release archive to extract the executable and input samples.
3. Export API credential token as environment variable: export IC_API_KEY="IBM Cloud API Key"

## Usage

1. Customize input samples.

2. Execute terraformer:
- Display help:\
terraformer -h
- Display version:\
terraformer --version
- Use Gen2, output directory, add prefix, Dallas region:\
terraformer -o output -p prefix -r Dallas input/access.xlsx\
terraformer -o output -p prefix -r Dallas input/lb.xlsx\
terraformer -o output -p prefix -r Dallas input/vpc.xlsx
- Use Gen1, output directory, add prefix, Dallas region:\
terraformer -g 1 -o output -p prefix -r Dallas input/access.xlsx\
terraformer -g 1 -o output -p prefix -r Dallas input/lb.xlsx\
terraformer -g 1 -o output -p prefix -r Dallas input/vpc.xlsx

3. Execute terraform in output directory:\
terraform fmt\
terraform init\
terraform plan\
terraform apply\
terraform destroy

## Regions

| Regions | Zones | Notes |
| --- | --- | --- |
| Dallas | Dallas 1,2,3 | |
| Frankfurt | Frankfurt 1,2,3 | Gen1 only. |
| London | London 1,2,3 | |
| Sydney | Sydney 1,2,3 | Gen1 only. |
| Tokyo | Tokyo 1,2,3 | Gen1 only. |
| Washington DC | Washington DC 1,2,3 | |

## Images (IBM-provided)

| Name | Arch | Description | Notes |
| --- | --- | --- | --- |
| ibm-centos7-amd64 | amd64 | CentOS 7.x - Minimal Install | |
| ibm-debian9-amd64 | amd64 | Debian GNU/Linux 9.x - Minimal Install | |
| ibm-redhat7-amd64 | amd64 | Red Hat Enterprise Linux 7.x - Minimal Install | |
| ibm-ubuntu16-amd64 | amd64 | Ubuntu Linux 16.04 LTS - Minimal Install | |
| ibm-ubuntu18-amd64 | amd64 | Ubuntu Linux 18.04 LTS - Minimal Install | |
| ibm-windows2012-amd64 | amd64 | Windows Server 2012 Standard Edition | |
| ibm-windows2012r2-amd64 | amd64 | Windows Server 2012 R2 Standard Edition | |
| ibm-windows2016-amd64 | amd64 | Windows Server 2016 Standard Edition | |
| ibm-centos7-ppc64le | ppc64le | CentOS 7.x - Minimal Install | Gen2 only. |
| ibm-debian9-ppc64le | ppc64le | Debian GNU/Linux 9.x - Minimal Install | Gen2 only. |
| ibm-ubuntu18-ppc64le | ppc64le | Ubuntu Linux 18.04 LTS - Minimal Install | Gen2 only. |

## Implementation

| Component | Description |
| --- | --- |
| General |  All fields, custom images, and secondary NICs need further testing. |
| | Additional fields in floatingips and publicgateways sheets are not yet supported. |
| | Additional resource-specific fields such as count are a future consideration. |
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
