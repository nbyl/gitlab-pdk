import argparse
import subprocess
import os
import sys

def extract_path(image):
  index = image.rindex("/")
  return image[0:index]

parser = argparse.ArgumentParser(description='Download a list of OCI images to a directory.')
parser.add_argument('--image-list', default='/tmp/pdk-image-list', help='location of the image list (default: /tmp/pdk-image-list)')
parser.add_argument('--image-directory', default='/tmp/pdk-images', help='location of the image list (default: /tmp/pdk-images)')
args = parser.parse_args()

images = []
with open(args.image_list, 'r') as image_list_file:
  for image in image_list_file:
    images.append(image.strip())

print("Starting dowload for " + str(len(images)) + " images.")
subprocess.call(["oc", "apply", "-f", os.path.dirname(sys.argv[0]) + "/../kubernetes/download-pod.yaml"])

for image in images:
  print("Extracting image " + image)
  image_path = extract_path(image)
  subprocess.call(["oc", "exec", "pdk-download-pod", "--", "mkdir", "-p", "/images/" + image_path])
  subprocess.call(["mkdir", "-p", args.image_directory + "/" + image_path])

  subprocess.call(["oc", "exec", "pdk-download-pod", "--", "skopeo", "copy", "docker://" + image, "dir://images/" + image_path, "--src-tls-verify=false"])
  subprocess.call(["oc", "rsync", "pdk-download-pod:/images/" + image_path, args.image_directory + "/" + image_path])

subprocess.call(["oc", "delete", "pod", "pdk-download-pod"])
