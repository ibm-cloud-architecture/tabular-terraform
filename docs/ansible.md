# Transform tabularized Terraform data into Terraform resources

## Install Ansible executables

1. [Download and install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

## Customize Ansible files 

1. Modify path of terraform.tfstate in ansible/inventory/terraform_inv.ini to match your location.

[TFSTATE]
TFSTATE_FILE = /terraform_plan_directory/terraform.tfstate

2. Copy ansible/inventory/group_vars/all-sample.yaml to all.yaml and modify:

dbpassword
logdna_key
sysgig_key 

## Create Terraform resources and apply

1. Execute the transform executable with your input data folder and output resources folder:  
    - bin/transform -o resources data
2. Execute Terraform in your resources folder:
    - terraform fmt
    - terraform init
    - terraform plan
    - terraform apply

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
