import os

def load(file):
  images = []

  with open(file, 'r') as image_list_file:
    for image in image_list_file:
      images.append(image.strip())

  return images

def save(file, images):
  with open(file, 'w') as image_list_file:
    for image in images.keys():
      image_list_file.write(image + '\n')
