'''
  File name: rmVerSeam.py
  Author: Luoli Wang
  Date created: 10.24.2019
'''
'''
    File clarification:
        Reads original image
        Calls the ‘carv’ function 
        Prints out the carved image
        nr, nc : the number of removed horizontal and vertical seams respectively 
'''
import numpy as np
import matplotlib.pyplot as plt
from carv import carv
from PIL import Image

if __name__ == "__main__":
    # I = np.array(Image.open('illusion_original.jpg').convert('RGB'))
    # I = np.array(Image.open('museo_original.jpg').convert('RGB'))
    # I = np.array(Image.open('frog_original.png').convert('RGB'))
    I = np.array(Image.open('monalisa.jpg').convert('RGB'))

    nr = 30
    nc = 30

    Ic, T = carv(I, nr, nc)
    print("Finised!")
    plt.imshow(Ic)
    plt.show()
