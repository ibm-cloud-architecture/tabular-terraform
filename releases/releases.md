# Terraformer Releases

### Terraformer v1.5.0.0 (Latest)

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.5.0.0/terraformer_1.5.0.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.5.0.0/terraformer_1.5.0.0_windows_amd64.zip) |
| [source](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.5.0.0/terraformer_source_1.5.0.0.zip) |

Changes:
- Upgraded to Provider v1.5.0 with new ibm_is_lb_listener_policy and ibm_is_lb_listener_policy_rule resources.
- Added data for lbpolicies and lbrules but not enabled yet.
- Added missing health_monitor_port optional column and field to lb/lbpools.
- Corrected health_monitor_url from required to optional in lb/lbpools.

### Terraformer v1.4.0.1

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.1/terraformer_1.4.0.1_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.1/terraformer_1.4.0.1_windows_amd64.zip) |

Changes:
- Initial code prep/test to include source code soon.

### Terraformer v1.4.0.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.0/terraformer_1.4.0.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.0/terraformer_1.4.0.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.4.0 which added resource_group to ibm_is_network_acl.
- Added resource_group column and field to access/aclheaders.

### Terraformer v1.3.0.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.3.0.0/terraformer_1.3.0.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.3.0.0/terraformer_1.3.0.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.3.0.

Note:\
Address prefix in data samples is available again.

---

### Terraformer v1.2.6.0 (Latest)

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.6.0/terraformer_1.2.6.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.6.0/terraformer_1.2.6.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.6.

Note:\
Opened VPC case where setting the address prefix to not assign default addresses leaves the VPC creation in Pending state.  Remove manual setting for address prefix in data samples until this VPC case has been resolved.

---

### Terraformer v1.2.5.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.5.0/terraformer_1.2.5.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.5.0/terraformer_1.2.5.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.5.
- Added support for json, ods, and yaml.

---

### Terraformer v1.2.4.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.4.0/terraformer_1.2.4.0_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.4.0/terraformer_1.2.4.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.4.
- Accept input directory to process all sheets with single command.

---

### Terraformer v1.2.3.4

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.3.4/terraformer_1.2.3.4_darwin_amd64.zip) |
| [windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.3.4/terraformer_1.2.3.4_windows_amd64.zip) |

Changes:
- Added support for Washington DC on Gen1 and Gen2, London on Gen2.
- Added support for RedHat, Windows, Power images on Gen2, refreshed all images to latest.
- Added -d command option (experimental).

---

Return to [README](/README.md)
