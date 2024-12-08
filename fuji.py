import csv
import numpy as np
from PIL import Image


def main():
    with open("fuji.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calc_brightness(f"{row['id']}.jpg")
            print(round(brightness, 2))
            

def calc_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L")))/255
    return brightness


main()