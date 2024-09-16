from PIL import Image
import matplotlib.pyplot as plt
import os

def test(name):
    img = Image.open(f"{os.path.dirname(__file__)}/memes/{name}")
    plt.imshow(img)
    plt.axis('off')
    plt.show()

test('i.png')