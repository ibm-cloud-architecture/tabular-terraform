# Generated by tabular-terraform
variable "vpc-name" {
  description = "Define vpc"
}
variable "resource-group" {
  description = "Define resource group"
}
variable "region" {
  description = "Define region"
}
variable "zone1" {
  description = "Define zone1"
}
variable "zone2" {
  description = "Define zone2"
}
variable "dbtier-subnet-zone1" {
  description = "Define dbtier subnet cidr for zone1"
}
variable "dbtier-subnet-zone2" {
  description = "Define dbtier subnet cidr for zone2"
}
variable "dbserver-name" {
  description = "Define db instance name"
}
variable "dbserver-count" {
  description = "Define db instance count"
}
variable "profile-dbserver" {
  description = "Define db instance profile"
}
variable "image" {
  description = "Define OS image for compute instances"
}
variable "vpc-id" {
  description = "Get vpc id"
}
variable "group-id" {
  description = "Get resource group id"
}
variable "sshkey-id" {
  description = "Get ssh key id"
}
variable "dbtier-subnet-zone1-id" {
  description = "Get dbtier subnet zone1 id"
}
variable "dbtier-subnet-zone2-id" {
  description = "Get dbtier subnet zone2 id"
}
variable "dbtier-securitygroup-id" {
  description = "Get dbtier security group id"
}
variable "maintenance-securitygroup-id" {
  description = "Get maintenance security group id"
}
