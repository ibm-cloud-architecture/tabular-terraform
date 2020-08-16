resource "null_resource" "cluster" {

  triggers = {
    cluster_instance_ids = "ibm_is_subnet.webapptier-subnet-zone1.id, ibm_is_subnet.webapptier-subnet-zone2.id, ibm_is_subnet.webapptier-subnet-zone1.id, ibm_is_subnet.webapptier-subnet-zone2.id"
  }

  provisioner "local-exec" {
    command = "sleep 300"
    when    = destroy
  }
}
