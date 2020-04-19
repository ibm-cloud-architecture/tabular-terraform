# Terraformer Releases

### Terraformer v1.4.0.0 (Latest)

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.0/terraformer_1.4.0.0_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.4.0.0/terraformer_1.4.0.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.4.0 which added resource_group to ibm_is_network_acl..
- Added resource_group column/field to access/aclheaders.

### Terraformer v1.3.0.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.3.0.0/terraformer_1.3.0.0_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.3.0.0/terraformer_1.3.0.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.3.0.

Note:\
Address prefix in data samples is available again.

---

### Terraformer v1.2.6.0 (Latest)

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.6.0/terraformer_1.2.6.0_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.6.0/terraformer_1.2.6.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.6.

Note:\
Opened VPC case where setting the address prefix to not assign default addresses leaves the VPC creation in Pending state.  Remove manual setting for address prefix in data samples until this VPC case has been resolved.

---

### Terraformer v1.2.5.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.5.0/terraformer_1.2.5.0_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.5.0/terraformer_1.2.5.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.5.
- Added support for json, ods, and yaml.

---

### Terraformer v1.2.4.0

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.4.0/terraformer_1.2.4.0_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.4.0/terraformer_1.2.4.0_windows_amd64.zip) |

Changes:
- Upgraded to Provider v1.2.4.
- Accept input directory to process all sheets with single command.

---

### Terraformer v1.2.3.4

| Assets |
| --- |
| [macOS 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.3.4/terraformer_1.2.3.4_darwin_amd64.zip) |
| [Windows 64-bit](https://github.com/ibm-cloud-architecture/terraformer/raw/master/releases/download/v1.2.3.4/terraformer_1.2.3.4_windows_amd64.zip) |

Changes:
- Added support for Washington DC on Gen1 and Gen2, London on Gen2.
- Added support for RedHat, Windows, Power images on Gen2, refreshed all images to latest.
- Added -d command option (experimental).

---

Return to [README](/README.md)
