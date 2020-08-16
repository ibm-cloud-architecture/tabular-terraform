# Terraformer for IBM Virtual Private Cloud

## Overview

- Terraformer handles the creation of Terraform syntax leaving the user to focus on the creation of data that is used by Terraformer in creating the Terraform files.
- For new Terraform users, Terraformer helps to get on the Terraform bandwagon by using and learning Terraform without focusing on the Terraform syntax. 
- For experienced Terraform users, Terraformer helps to expedite the implementation of Terraform, or Terraformer can be used on individual parts of a Terraform implementation such as the rules for ACLs and Security Groups.
- Terraformer is provided with no formal support but problems can be reported by opening a GitHub issue.
- Data format is subject to change.

<details><summary>Examples</summary>
<p>

![TerraformerInputExample](/images/terraformerinputexample.png)
![TerraformerOutputExample](/images/terraformeroutputexample.png)

</p>
</details>

## Requirements

- IBM Cloud Terraform Provider v1.10.0
- Terraform v0.12.23
- Ansible 2.9.11
- Python v3.8.2
- Cython v0.29.15

## Installation

1. [Download Terraformer](/releases/releases.md) (Latest: v1.10.0.0).
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

1. Copy sample files from provided data folder to your folder. 

2. Customize sample files with the infrastructure to be provisioned.

3. To display command options:  bin/terraformer -h

4. To generate Terraform with input from data folder and output to resources/vpc folder:  bin/terraformer -o resources/vpc data

5. Execute terraform in output directory to provision your VPC infrastructure:\
terraform fmt\
terraform init\
terraform plan\
terraform apply

## Notes

<details><summary>Implementation</summary>
<p>

| Component | Description |
| --- | --- |
| Sheets | Asterisk in column name denotes a required field. |
| | Rerun Terraformer after changing data and rely on Terraform to handle changes. 
| | Sheet names can be basename (e.g. instances) or basename-groupname (e.g. instances-group1) to organize data of same type into separate sheets.
| | Sheet columns are subject to change. |

</p>
</details>

</p>
</details>

## References

1. [IBM Cloud Stencils](https://github.com/ibm-cloud-architecture/ibm-cloud-stencils)
2. [IBM Terraformer Provider](https://github.com/IBM-Cloud/terraform-provider-ibm)

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
