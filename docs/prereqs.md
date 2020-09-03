# Prerequisite Steps

## Install prerequisite software

1. [Download and install Terraform](https://www.terraform.io/downloads.html)
2. [Download IBM Cloud Terraform Provider](https://github.com/IBM-Cloud/terraform-provider-ibm/releases)
3. Unzip the provider release archive and move the plugins binary into the Terraform plugins directory for the platform.
4. [Download and install Ansible](https://docs.ansible.com/ansible/latest/index.html)
5. [Download and install Python 3](https://www.python.org/downloads/)
6. Install Python 3 libraries:
    - numpy
    - pandas
    - cython (for compiling)
    - xlrd (for xlsx)
    - odfpy (for ods)
    - pyyaml (for yaml)

Note: Install Python 3 from python.org separately from Mac default of Python 2 - installing with brew, pipenv, or pyenv use different directories that won't work.

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
