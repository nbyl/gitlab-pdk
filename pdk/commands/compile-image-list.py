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
import array
import io
import yaml
import pdk.image_list

parser = argparse.ArgumentParser(description='Compile a list of images to retrieve from a .gitlab-ci.yml file.')
parser.add_argument('--image-list', default='/tmp/pdk-image-list', help='an integer for the accumulator (default: /tmp/pdk-image-list)')
args = parser.parse_args()

images = {}
with open(".gitlab-ci.yml", 'r') as stream:
  gitlab_pipeline = yaml.safe_load(stream)

  for job in gitlab_pipeline:
    if isinstance(gitlab_pipeline[job],dict) and 'image' in gitlab_pipeline[job].keys():
      images[gitlab_pipeline[job]['image']] = True

  pdk.image_list.save(args.image_list, images)

print("Successfully wrote image list to " + args.image_list)
