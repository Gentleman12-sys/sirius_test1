from PIL import Image
import matplotlib.pyplot as plt

def test(name):
    img = Image.open(f"memes/{name}")
    plt.imshow(img)
    plt.axis('off')
    plt.show()

test('i.png')