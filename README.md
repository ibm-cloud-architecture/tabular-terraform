# Terraformer for IBM Virtual Private Cloud

## Overview

- Terraformer handles the creation of Terraform syntax leaving the user to focus on the creation of data that is used by Terraformer in creating the Terraform files.
- For new Terraform users, Terraformer helps to get on the Terraform bandwagon by using and learning Terraform without focusing on the Terraform syntax. 
- For experienced Terraform users, Terraformer helps to expedite the implementation of Terraform, or Terraformer can be used on individual parts of a Terraform implementation such as the rules for ACLs and Security Groups.
- Terraformer is provided with no formal support but problems can be reported by opening a GitHub issue.
- Data format is subject to change.

## Prerequisites

The following software needs to be installed
1. Terraform v0.12.23+](https://www.terraform.io/downloads.html)
2. IBM Cloud Terraform Provider v1.10.0](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
3. [Ansible 2.9.11](https://docs.ansible.com/ansible/latest/index.html)
4. [Python v3.8.2](https://www.python.org/downloads/) with libraries:
- numpy
- pandas
- cython (for compiling)
- xlrd (for xlsx)
- odfpy (for ods)
- pyyaml (for yaml)

Note: Mac default is Python 2 so Python 3 needs to be installed separately from python.org - installing with brew, pipenv, or pyenv installs libraries into different directories that won't work with Terraformer.

## Usage

1. [Download Terraformer v1.10.0.1](/releases/releases.md)

2. Unzip terraformer archive.

3. Copy sample files from provided data folder to your folder. 

4. Customize sample files with the infrastructure to be provisioned.

5. To display command options:  bin/terraformer -h

6. To generate Terraform with input from data directory and output to resources/vpc directory:  bin/terraformer -o resources/vpc data

7. Execute terraform in output directory to provision your VPC infrastructure:\
terraform fmt\
terraform init\
terraform plan\
terraform apply

## Notes

| Implementation Notes |
| --- |
| Asterisk in column name denotes a required field. |
| Rerun Terraformer after changing data and rely on Terraform to handle changes. |
| Sheet names can be either basename (e.g. instances) or basename-groupname (e.g. instances-group1) to organize data of same type into separate sheets. |
| Data is copied directly to generated Terraform (e.g. include quotes on data for strings, no quotes for numeric data, etc). |
| The variables-system sheet is provided either as reference or using with var to facilitate adding image IDs to instances.  If an image ID is changed in the VPC product or additional images added, this sheet can be updated directly or should be updated in a future Terraformer release or define your own variables for image IDs. |

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
