# Terraformer for IBM Virtual Private Cloud
#
# Copyright IBM Corporation 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Zones

# @revisit move all constants to variables in data.

gen1regionsdictionary = {
'Dallas': 'us-south',
'Frankfurt': 'eu-de',
'London': 'eu-gb',
'Sydney': 'au-syd',
'Tokyo': 'jp-tok',
'WashingtonDC': 'us-east'
}

gen2regionsdictionary = {
'Dallas': 'us-south',
'Frankfurt': 'eu-de',
'London': 'us-gb',
'WashingtonDC': 'us-east'
}

gen1zonesdictionary = {
'Dallas1': 'us-south-1',
'Dallas2': 'us-south-2',
'Dallas3': 'us-south-3',
'Frankfurt1': 'eu-de-1',
'Frankfurt2': 'eu-de-2',
'Frankfurt3': 'eu-de-3',
'London1': 'eu-gb-1',
'London2': 'eu-gb-2',
'London3': 'eu-gb-3',
'Sydney1': 'au-syd-1',
'Sydney2': 'au-syd-2',
'Sydney3': 'au-syd-3',
'Tokyo1': 'jp-tok-3',
'Tokyo2': 'jp-tok-2',
'Tokyo3': 'jp-tok-3',
'WashingtonDC1': 'us-east-1',
'WashingtonDC2': 'us-east-2',
'WashingtonDC3': 'us-east-3'
}

gen2zonesdictionary = {
'Dallas1': 'us-south-1',
'Dallas2': 'us-south-2',
'Dallas3': 'us-south-3',
'Frankfurt1': 'eu-de-1',
'Frankfurt2': 'eu-de-2',
'Frankfurt3': 'eu-de-3',
'London1': 'eu-gb-1',
'London2': 'eu-gb-2',
'London3': 'eu-gb-3',
'WashingtonDC1': 'us-east-1',
'WashingtonDC2': 'us-east-2',
'WashingtonDC3': 'us-east-3'
}

gen1imageprofilesdictionary = {
# Intel image profiles
'bx2-2x8': 'bc1-2x8',
'bx2-4x16': 'bc1-4x16',
'bx2-8x32': 'bc1-8x32',
'bx2-16x64': 'bc1-16x64',
'bx2-32x128': 'bc1-32x128',
'bx2-48x192': 'bc1-48x192',
'bx2-62x248': 'bc1-62x248', # Gen1 only.
'cx2-2x4': 'cc1-2x4',
'cx2-4x8': 'cc1-4x8',
'cx2-8x16': 'cc1-8x16',
'cx2-16x32': 'cc1-16x32',
'cx2-32x64': 'cc1-32x64',
'mx2-2x16': 'mc1-2x16',
'mx2-4x32': 'mc1-4x32',
'mx2-8x64': 'mc1-8x64',
'mx2-16x128': 'mc1-16x128',
'mx2-32x256': 'mc1-32x256'
}

gen2imageprofilesdictionary = {
# Intel image profiles
'bx2-2x8': 'bx2-2x8',
'bx2-4x16': 'bx2-4x16',
'bx2-8x32': 'bx2-8x32',
'bx2-16x64': 'bx2-16x64',
'bx2-32x128': 'bx2-32x128',
'bx2-48x192': 'bx2-48x192',
'cx2-2x4': 'cx2-2x4',
'cx2-4x8': 'cx2-4x8',
'cx2-8x16': 'cx2-8x16',
'cx2-16x32': 'cx2-16x32',
'cx2-32x64': 'cx2-32x64',
'mx2-2x16': 'mx2-2x16',
'mx2-4x32': 'mx2-4x32',
'mx2-8x64': 'mx2-8x64',
'mx2-16x128': 'mx2-16x128',
'mx2-32x256': 'mx2-32x256',
# Power image profiles
'bp2-2x8': 'bp2-2x8',
'bp2-4x16': 'bp2-4x16',
'bp2-8x32': 'bp2-8x32',
'bp2-16x64': 'bp2-16x64',
'bp2-32x128': 'bp2-32x128',
'cp2-2x4': 'cp2-2x4',
'cp2-4x8': 'cp2-4x8',
'cp2-8x16': 'cp2-8x16',
'cp2-16x32': 'cp2-16x32',
'cp2-32x64': 'cp2-32x64',
'gp2-8x64x2': 'gp2-8x64x2',
'gp2-16x128x2': 'gp2-16x128x2',
'gp2-16x128x4': 'gp2-16x128x4',
'gp2-24x224x2': 'gp2-8x224x2',
'gp2-32x256x4': 'gp2-8x256x4',
'gp2-56x448x4': 'gp2-8x448x4',
'gp2-56x896x4': 'gp2-8x896x4',
'mp2-2x16': 'mp2-2x16',
'mp2-2x32': 'mp2-2x32',
'mp2-4x32': 'mp2-4x32',
'mp2-4x64': 'mp2-4x64',
'mp2-8x64': 'mp2-8x64',
'mp2-16x128': 'mp2-16x128',
'mp2-32x256': 'mp2-32x256',
'mp2-48x768': 'mp2-48x768'
}

# Images

gen1imagedictionary = {
# Intel images
'ibm-centos7-amd64': '6aec77ca-ab4a-459e-81dc-6e5ec9f99d4a',
'ibm-debian9-amd64': 'e578762f-22e2-448b-8eac-1452d8399e4c',
'ibm-redhat7-amd64': '54c1ba68-6d29-42e5-9ca7-e5f4a62c1503',
'ibm-ubuntu16-amd64': '683a4222-b6bc-499f-bd3b-8b90b3ccfd86',
'ibm-ubuntu18-amd64': 'fc538f61-7dd6-4408-978c-c6b85b69fe76',
'ibm-windows2012-amd64': 'a7a0626c-f97e-4180-afbe-0331ec62f32a',
'ibm-windows2012r2-amd64': '51af68c9-5558-4425-825a-f9243a3b2c6c',
'ibm-windows-2016-amd64': '624cde4a-b4fe-4426-8f60-150a019a67f9'
}

gen2imagedictionary = {
# Intel images
'ibm-centos7-amd64': 'r006-e0039ab2-fcc8-11e9-8a36-6ffb6501dd33',
'ibm-debian9-amd64': 'r006-d4aec81e-fcc6-11e9-9149-870ebf69fd8d',
'ibm-redhat7-amd64': 'r006-931515d2-fcc3-11e9-896d-3baa2797200f',
'ibm-ubuntu16-amd64': 'r006-34ceeafe-fcc6-11e9-893a-57dde2f48a21',
'ibm-ubuntu18-amd64': 'r006-14140f94-fcc4-11e9-96e7-a72723715315',
'ibm-windows2012-amd64': 'r006-5f9568ae-792e-47e1-a710-5538b2bdfca7',
'ibm-windows2012r2-amd64': 'r006-8bb3e8aa-b789-4292-8679-3564b3a9366a',
'ibm-windows-2016-amd64': 'r006-54e9238a-ffdd-4f90-9742-7424eb2b9ff1',
# Power images
'ibm-centos7-ppc64le': 'r006-a5636224-fcce-11e9-8542-cf9657fdcaa3',
'ibm-debian9-ppc64le': 'r006-67ca3f5a-fcce-11e9-a809-73839369f0fc',
'ibm-ubuntu18-ppc64le': 'r006-d2f5be47-f7fb-4e6e-b4ab-87734fd8d12b'
}

# Volume Profiles

gen1volumeprofilesdictionary = {
'general-purpose': 'general-purpose', # 3iops-tier
'5iops-tier': '5iops-tier',
'10iops-tier': '10iops-tier',
'custom': 'custom'
}

gen2volumeprofilesdictionary = {
'general-purpose': 'general-purpose', # 3iops-tier
'5iops-tier': '5iops-tier',
'10iops-tier': '10iops-tier',
'custom': 'custom'
}
