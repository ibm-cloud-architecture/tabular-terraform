# Terraformer for IBM Virtual Private Cloud

## Overview

- Create Terraform resources from user data.
- Start learning Terraform with the help of Terraformer.
- Expedite a Terraform implementation or parts such as network ACLs and Security Groups.
- Provided with no formal support but problems can be reported by opening a GitHub issue.
- Data format is subject to change.

## Prerequisites

Install the following software:
1. [Terraform v0.12.23+](https://www.terraform.io/downloads.html)
2. [IBM Cloud Terraform Provider v1.10.0](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
3. [Ansible 2.9.11](https://docs.ansible.com/ansible/latest/index.html)
4. [Python v3.8.2](https://www.python.org/downloads/) with libraries:
    - numpy
    - pandas
    - cython (for compiling)
    - xlrd (for xlsx)
    - odfpy (for ods)
    - pyyaml (for yaml)

Note: Install Python 3 from python.org separately from Mac default of Python - installing with brew, pipenv, or pyenv use different directories that won't work.

## Deploy VPC Infrastructure using Terraform and Ansible

1. [Deploy Infrastructure using Terraform)(/docs/terraform.md)
2. TBD

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
