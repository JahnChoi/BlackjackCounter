import urllib.request
import cv2
import numpy as np

import io
import os
from google.cloud import vision
from google.cloud.vision import types

def get_labels(content):
    vision_client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)
    response = vision_client.label_detection(image=image)

    return response.label_annotations


def detect_logos(content):
    """Detects popular logos in the file."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations

    return logos


def detect_text(content):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


def detect_properties(content):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))


def detect_document(content):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))


def detect_web(content):
    """Detects web annotations given an image."""
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    notes = response.web_detection

    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in notes.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print ('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
            

if __name__ == '__main__':
    url = 'http://10.30.5.61:8080/shot.jpg?rnd=275367'
    
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    cv2.imwrite('camera.png', img)

    with io.open('camera.png', 'rb') as image_file:
        content = image_file.read()

    detect_web(content)

    #detect_document(content)

    #detect_properties(content)

    #detect_text(content)

    #logos = detect_logos(content)

    #for logo in logos:
    #    print(logo.description)

    #labels = get_labels(content)

    #for label in labels:
    #    print(label.mid, end=' ')
    #    print(label.description, end=' ')
    #    print(label.score)