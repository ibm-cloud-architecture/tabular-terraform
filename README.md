# Tabular Terraform - Transform tabularized Terraform to Terraform resources.

## Overview

- Latest release: [Terraformer 1.11.1.0](/releases/releases.md)
- Improves viewability and maintainability of Terraform.
- For simple usage, use constants and resource references in data.
- For complex usage, also include functional references in data.
- For partial usage, only represent specific components in data (e.g. network ACLs, Security Groups, etc).
- Tabular representation may not be possible for every resource or field but can be useful where possible.
- Provided with no formal support but problems can be reported by opening a GitHub issue.
- Data format is subject to change.

## Implementation

1. For column names, asterisk denotes a required field.
2. For complex lists, add number to group name in new column (e.g. network_interfaces2.subnet).
3. For data fields, values are copied directly to generated Terraform.
4. For sheet names, use either basename (e.g. instances) or basename-groupname (e.g. instances-group1).
5. For OS images, variables-system sheet is provided for reference but is subject to change.
6. For changed data, regenerate Terraform and let Terraform handle changes. 
7. For directory backups, when generating Terraform an existing directory is backed up to directory.backupNNN. 

## Prerequisites

Install the following software:
1. [IBM Cloud Terraform Provider v1.11.1](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
2. [Terraform v0.12.23+](https://www.terraform.io/downloads.html)
3. [Ansible 2.9.11](https://docs.ansible.com/ansible/latest/index.html)
4. [Python v3.8.2](https://www.python.org/downloads/) with libraries:
    - numpy
    - pandas
    - cython (for compiling)
    - xlrd (for xlsx)
    - odfpy (for ods)
    - pyyaml (for yaml)

Note: Install Python 3 from python.org separately from Mac default of Python 2 - installing with brew, pipenv, or pyenv use different directories that won't work.

## Deploy VPC Infrastructure using Terraform and Ansible

1. [Deploy Infrastructure using Terraform](/docs/terraform.md)
2. TBD

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
