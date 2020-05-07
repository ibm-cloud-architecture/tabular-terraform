# Terraformer Development

## Overview

## Requirements

- IBM Cloud Terraform Provider v1.5.0
- Terraform v0.12.23
- Python v3.8.2
- Cython v0.29.15 (optional)

## Development Needs

| Area | Need | Description |
| --- | --- | --- |
| Build | Get scripts/savebuildmac.sh working and convert to makefile. | The source was a single file that worked fine with Cython until the source was split into multiple files for maintainability - the compile and link complete but running the executable is unable to find the symbols in the separate files.  The scripts/buildmac.sh is a temporary workaround to combine the files back into a single source file to work with Cython. |
| All | Test all data fields and variations. | Testing is mostly done with the provided data which doesn't use all fields.  Testing needs to be done with all fields. |
| Images | Test custom images and fix as needed. | Images are implemented but tested with provided images.  Custom images need to be tested. |
| NICs | Test secondary NICs and fix as needed. | NICs are implemented but tested with primary NICs.  Secondary NICs need to be tested. |
| LB | Complete coding for the new LB policies and rules. | Data has been added for the LB policies and rules but coding and testing needs to be done. |

## License

This application is licensed under the Apache License, Version 2.  Separate third-party code objects invoked by this application are licensed by their respective providers pursuant to their own separate licenses.  Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).
