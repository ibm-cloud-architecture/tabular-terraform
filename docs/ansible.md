# Ansible Steps

## Customize Ansible files 

1. Modify path of terraform.tfstate in playbooks/inventory/terraform_inv.ini to match your location:
- TFSTATE_FILE = /terraform_plan_directory/terraform.tfstate

2. Copy playbooks/inventory/group_vars/all-sample.yaml to all.yaml and modify:
- dbpassword
- logdna_key
- sysgig_key 


## Execute Ansible

1. Verify execution of dynamic inventory script with output that shows hosts and groups:
- ansible-playbook -i inventory site.yaml --list-hosts

2. Verify execution of tasks to be applied in each play (common, web, and db):
- ansible-playbook -i inventory site.yaml --list-tasks 

3. Before executing plays, verify the post porovisioning process has completed:
- cloud-init status

4. Execute the plays:
- ansible-playbook -i inventory --ssh-extra-args='-J root@your-bastion-IP' site.yaml

5. After the playbook has completed, open a browser and enter the URL specified in the Terraform variables.

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
