import numpy as np
from ipywidgets import interact, fixed
from PIL import Image


def imshow(X, resize=None):
    new_im = Image.fromarray(X)
    if resize:
        new_im= new_im.resize(resize)
    return plt.imshow(new_im)
