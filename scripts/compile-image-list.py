import argparse
import array
import io
import yaml

parser = argparse.ArgumentParser(description='Compile a list of images to retrieve from a .gitlab-ci.yml file.')
parser.add_argument('--image-list', default='/tmp/pdk-image-list', help='an integer for the accumulator (default: /tmp/pdk-image-list)')
args = parser.parse_args()

images = {}
with open(".gitlab-ci.yml", 'r') as stream:
  gitlab_pipeline = yaml.safe_load(stream)

  for job in gitlab_pipeline:
    if isinstance(gitlab_pipeline[job],dict) and 'image' in gitlab_pipeline[job].keys():
      images[gitlab_pipeline[job]['image']] = True

with open(args.image_list, 'w') as image_list_file:
  for image in images.keys():
    image_list_file.write(image + '\n')

print("Successfully wrote image list to " + args.image_list)
