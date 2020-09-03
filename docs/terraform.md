# Transform tabularized Terraform data into Terraform resources

## Install Terraform executables

1. [Download and install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
2. [Download IBM Cloud provider plugin for Terraform](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
3. Unzip the provider release archive and move the plugins binary into the Terraform plugins directory for the platform.
4. [Download tabular-terraform](/releases/releases.md)
5. Unzip the tabular-terraform release archive into a location as desired.

## Customize Terraform data

1. Modify vars spreadsheet as desired including:
    - vpc-name
    - resource-group
    - cis-resource-group
    - domain
    - cis-instance-name 
2. Modify other spreadsheets as desired.
3. Modify terraform/cloudinits as desired.

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
