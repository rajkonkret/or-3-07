import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img = mpimg.imread('user_photo.jpg')

plt.imshow(img)
plt.axis('off')
plt.show()

# wczytanie obrazka z apomocą PIL
image = Image.open('user_photo.jpg')

image.show()
