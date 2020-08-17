# Terraformer for IBM Virtual Private Cloud

## Deploying VPC Infrastructure using Terraform

## Modify sample Terraform resources

1. [Download and install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
2. [Download IBM Cloud provider plugin for Terraform](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
3. Unzip the provider release archive and move the plugins binary into the Terraform plugins directory for the platform.
4. [Download Terraformer](/releases/releases.md)
5. Unzip the terraformer release archive into a location of your choosing.
6. Modify the vars spreadsheet (variables.tf) for the following variables:
    - TBD
7. Execute Terraformer with your data files and output folder:  
    - bin/terraformer -o resources data
8. Execute Terraform in resources folder:
    - terraform fmt
    - terraform init
    - terraform plan
    - terraform apply

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
