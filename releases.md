# tabular-terraform releases

- 2.0.0 (07/04/21) : Added GUI and build dist app. 

- 1.19.0.0 : Upgraded to provider 1.19.0.
- 1.17.0.0 : Upgraded to provider 1.17.0.
- 1.14.0.1 : Added support for modules and provider 1.14.0.
- 1.13.1.0 : Added provider name and version to versions.tf, provider 1.13.1, terraform 0.13.5.
- 1.12.0.1 : Reorganized some sheets and files.
- 1.12.0.0 : Added Instance Group and Flow Logs sheets, provicer 1.12.0.
- 1.11.2.2 : Update generate files and output in webappvpc.
- 1.11.2.1 : Move data directory to webappvpc.
- 1.11.2.0 : Renamed tool, provider 1.11.2.
- 1.11.1.0 : Added Transit Gateweay sheet, provider 1.11.1.
- 1.11.0.0 : Added complex lists, provider 1.11.0.
- 1.10.0.2 : Added output directory backup and port 22 to ACL rules.
- 1.10.0.1 : Generate comments and outputs.
- 1.10.0.0 : Refactored, added CIS sheet, added webappvpc example with Ansible, provider 1.10.0.
- 1.9.0.0 : Provider 1.9.0. 
- 1.8.1.0 : Provider 1.8.1.
- 1.7.1.0 : Provider 1.7.1.
- 1.7.0.0 : Provider 1.7.0.
- 1.6.0.0 : Provider 1.6.0, changed encryption_algorithm value from 3des to aes256 on IKE/IPSec Policies.  Provider v1.6.0 changed 3des to triple_des but since the default value in the data had to be changed to match it was changed to aes to be more secure.
- 1.5.2.1 : Started support for puml.
- 1.5.2.0 : Provider 1.5.2, added structures for lbpolicies and lbrules but not enabled yet.
- 1.5.0.1 : Added Frankfurt support to Gen2 and var sheet.
- 1.5.0.0 : Provider 1.5.0, added lbpolicies and lbrules to lb sheet.
- 1.4.0.1 : Initial code prep/test to include source code soon.
- 1.4.0.0 : Provider 1.4.0, added resource_group column and field to access/aclheaders.
- 1.3.0.0 : Provider 1.3.0, address prefix in sample is available again.
- 1.2.6.0 : Provider 1.2.6, opened VPC case where setting the address prefix to not assign default addresses leaves the VPC creation in Pending state.  Remove manual setting for address prefix in data samples until this VPC case has been resolved.
- 1.2.5.0 : Provider 1.2.5, added support for json, ods, and yaml.
- 1.2.4.0 : Provider 1.2.4, added input directory to process all sheets.
- 1.2.3.4 : Added WDC on Gen1 and Gen2, London on Gen2, RedHat, Windows, Power images on Gen2, refreshed all images to latest.

Return to [README](/README.md)
