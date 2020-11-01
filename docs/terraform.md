# Terraform Steps

## Setup tabular-terraform files

1. [Download tabular-terraform](/releases/releases.md)
2. Unzip the tabular-terraform release archive into a location as desired.

## Customize tabular-terraform data

1. Modify vars spreadsheet as desired including:
- vpc-name
- resource-group
- cis-resource-group
- domain
- cis-instance-name 
2. Modify other spreadsheets as desired.
3. Modify cloudinits as desired.

## Create Terraform resources and apply

1. Execute the tabular-terraform transform executable with your input data folder and output resources folder:  
- bin/transform -o resources data
2. Execute Terraform in your resources folder:
- terraform fmt
- terraform init
- terraform plan
- terraform apply

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
