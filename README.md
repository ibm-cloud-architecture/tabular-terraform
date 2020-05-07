# Terraformer for IBM Virtual Private Cloud

## Overview

- Terraformer handles the creation of Terraform syntax leaving the user to focus on the creation of data (json, ods, xlsx, or yaml) that is used by Terraformer in creating the Terraform files.
- For new Terraform users, Terraformer helps to get on the Terraform bandwagon by using and learning Terraform without focusing on the Terraform syntax. 
- For experienced Terraform users, Terraformer helps to expedite the implementation of Terraform, or Terraformer can be used on individual parts of a Terraform implementation such as the rules for ACLs and Security Groups.
- Terraformer is provided with no formal support but problems can be reported by opening a GitHub issue.
- Data format is subject to change but a future consideration is to migrate data when format changes.

<details><summary>Examples</summary>
<p>

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample](/images/terraformeroutputexample.png)

</p>
</details>

## Requirements

- IBM Cloud Terraform Provider v1.5.0
- Terraform v0.12.23
- Python v3.8.2
- Cython v0.29.15 (optional)

## Installation

1. [Download Terraformer](/releases/releases.md) (Latest: v1.5.0.1).
- Unzip Terraformer archive to extract terraformer executable and sample data.
2. [Download and install Terraform](https://www.terraform.io/downloads.html).
- Unzip Terraform archive to extract terraform binary and add location to PATH. 
3. [Download and install IBM Cloud Terraform Provider](https://github.com/IBM-Cloud/terraform-provider-ibm/releases).
- Unzip provider archive to extract plugin binary and move to Terraform plugins directory.
- Export API credential token as environment variable: export IC_API_KEY="IBM Cloud API Key"
4. [Download and install Python 3](https://www.python.org/downloads/).
- Install numpy, pandas, xlrd (xlsx support), odfpy (ods support), and pyyaml (yaml support).
- Note: Mac comes with Python 2 by default so Python 3 needs to be installed separately from python.org - installing with brew, pipenv, or pyenv installs libraries into different directories that won't work with Terraformer.

## Usage

1. Design your VPC infrastructure using [IBM Cloud Stencils](https://github.com/ibm-cloud-architecture/ibm-cloud-stencils).

2. Copy sample files from provided json, ods, xlsx, or yaml folder to your data folder. 

3. Customize sample files according to your design.

4. To display command options:  bin/terraformer -h

5. To generate with input from data and output to resources:  bin/terraformer data

6. Execute terraform in output directory to provision your VPC infrastructure:\
terraform fmt\
terraform init\
terraform plan\
terraform apply

## Notes

<details><summary>Regions</summary>
<p>

| Regions | Zones | Notes |
| --- | --- | --- |
| Dallas | Dallas 1,2,3 | |
| Frankfurt | Frankfurt 1,2,3 | |
| London | London 1,2,3 | |
| Sydney | Sydney 1,2,3 | Gen1 only. |
| Tokyo | Tokyo 1,2,3 | Gen1 only. |
| Washington DC | Washington DC 1,2,3 | |

</p>
</details>

<details><summary>Images (IBM-provided)</summary>
<p>

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

</p>
</details>

<details><summary>Implementation</summary>
<p>

| Component | Description |
| --- | --- |
| General | Incomplete features: custom images, secondary NICs, LB policies, Power, fips, public gateways. |
| | Additional resource-specific fields such as count are a future consideration. |
| Files | Related resources are grouped into generated files. |
| | Rerun after changes and rely on Terraform to handle changes. |
| Sheets | Use name of basename-groupname for copied data (e.g. instances-group1). |
| | Columns are subject to change but no upgrade between data versions. |
| | Asterisk in column name denotes a required field. |
| Floating IP | Created from primary_nic_floating_ip or secondary NIC or subnet public_gateway. |
| | Move FIP to another NIC/Public Gateway and rely on Terraform to handle change. |
| | Use floatingips data to set additional arguments - not currently implemented. |
| Images | Profile names are Gen 1 or Gen 2 style - Gen 2 names are converted to Gen 1 names. |
| Public Gateway | Created from subnet public_gateway (e.g. gatewayname:optionalfipname). |  
| | Use publicgateways data to set additional arguments - not currently implemented. |
| Regions | Names are UI style or internal name (e.g. Dallas or us-south). |
| Resource Groups | Terraform destroy only removes state information but does not delete resource group.
| Volumes | Profile names are general-purpose, 5iops-tier, 10iops-tier, or custom. |
| | Only name and encryption are valid for boot volumes. |
| Zones | Names are UI style or internal name (e.g. Dallas 1 or us-south-1). |

</p>
</details>

<details><summary>Development</summary>
<p>

| Area | Need | Description |
| --- | --- | --- |
| Build | Get scripts/savebuildmac.sh working and convert to makefile. | The source was a single file that worked fine with Cython until the source was split into multiple files for maintainability - the compile and link complete but running the executable is unable to find the symbols in the separate files.  The scripts/buildmac.sh is a temporary workaround to combine the files back into a single source file to work with Cython. |
| All | Test all data fields and variations. | Testing is mostly done with the provided data which doesn't use all fields.  Testing needs to be done with all fields. |
| Images | Test custom images and fix as needed. | Images are implemented but tested with provided images.  Custom images need to be tested. |
| NICs | Test secondary NICs and fix as needed. | NICs are implemented but tested with primary NICs.  Secondary NICs need to be tested. |
| LB | Complete coding for the new LB policies and rules. | Data has been added for the LB policies and rules but coding and testing needs to be done. |

</p>
</details>

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
