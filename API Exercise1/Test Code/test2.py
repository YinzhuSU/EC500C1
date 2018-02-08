import io
import os

import google.cloud.vision

    # Create a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

    # TODO (Developer): Replace this with the name of the local image
    # file to analyze.
image_file_name = 'su.jpg'
with io.open(image_file_name, 'rb') as image_file:
    content = image_file.read()

    # Use Vision to label the image based on content.
image = google.cloud.vision.types.Image(content=content)
response = vision_client.label_detection(image=image)

print('Labels:')
for label in response.label_annotations:
    print(label.description)