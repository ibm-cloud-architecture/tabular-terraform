# Terraformer for IBM Virtual Private Cloud

Automate creation of Terraform for IBM Virtual Private Cloud.

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample12](/images/terraformeroutputexample12.png)

# Usage Steps

1. Export API credential token as an environment variable:\
export IC_API_KEY="IBM Cloud API Key"

2. Execute terraformer:
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
terraformer -g 1 -o gen1output -p prefix -r Dallas lp.xlsx\
terraformer -g 1 -o gen1output -p prefix -r Dallas vpc.xlsx

3. Execute terraform in specified output directory:\
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

# Implementation Notes

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
| | Utilizes resource name and target, but zone is not utilized. |
| | Create and delete timeouts use Terraform default of 10 minutes. |
| Images | Profile names are Gen 1 or Gen 2 style - Gen 2 names are converted to Gen 1 names. |
| Public Gateway | Created from subnet public_gateway (e.g. gatewayname:optionalfipname). |  
| | Utilizes resource name, vpc, and zone, but resource_controller_url is not utilized. |
| | Create and delete timeouts use Terraform default of 60 minutes. |
| Regions | Names are UI style or internal name (e.g. Dallas or us-south). |
| Resource Groups | Terraform destroy only removes state information but does not delete resource group.
| Rules | Protocols are icp:type:code, tcp:port_min:port_max, udp:port_min:port_max, or empty. | 
| | Protocols are problematic in 1.2.0 provider so access.xlsx has empty values for these until fixed. | 
| Volumes | Profile names are general-purpose, 5iops-tier, 10iops-tier, or custom. |
| | Only name and encryption are valid for boot volumes. |
| Zones | Names are UI style or internal name (e.g. Dallas 1 or us-south-1). |

# Release Notes

| Version | Released | Provider | Description |
| --- | --- | --- | --- |
| 1.2.0.0 | 2020-02-08 | 1.2.0 | Initial release with all VPC Gen2 resources in provider. |
