def extract_path(image):
  index = image.rindex("/")
  return image[0:index]

def extract_name(image):
  image = image.lstrip(extract_path(image)) 
  index = image.rindex("@")
  return image[0:index]