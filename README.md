# Transform tabularized Terraform data into Terraform resources

## Overview

- Latest release: 2.0.0](/releases/releases.md)
- Terraform data is maintained in spreadsheets where possible and transformed from spreadsheets into Terraform resources.
- Using spreadsheets improves viewability and maintainability of Terraform.
- Example webappvpc includes use of Terraform cloudinits and Ansible Playbooks to configure applications.
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

# Prerequisites

1. IBM Cloud Terraform Provider 1.19.0
2. Terraform 0.13.5
3. Ansible 2.9.11
4. Python 3.8.2

## Usage (Transitioning to Schematics)

1. [Install prerequisites](docs/prereqs.md)
2. [Deploy Infrastructure using Terraform](/docs/terraform.md)
3. [Configure applications using Ansible](/docs/ansible.md)

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
