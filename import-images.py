# Copyright 2019 Nicolas Byl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import pdk.image
import pdk.image_list
import subprocess

parser = argparse.ArgumentParser(description='Download a list of OCI images to a directory.')
parser.add_argument('--image-list', default='/tmp/pdk-image-list', help='location of the image list (default: /tmp/pdk-image-list)')
parser.add_argument('--image-directory', default='/tmp/pdk-images', help='location of the image list (default: /tmp/pdk-images)')
args = parser.parse_args()

images = pdk.image_list.load(args.image_list)

print("Starting dowload for " + str(len(images)) + " images.")

for image in images:
  print("Extracting image " + image)
  image_path = pdk.image.extract_path(image)

  subprocess.check_call(["docker", "import", args.image_directory + "/" + image_path + pdk.image.extract_name(image) + ".tar", image_path + pdk.image.extract_name(image)])


print("Done.")