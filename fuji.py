import csv
import numpy as np
from PIL import Image


def main():
    with open("fuji.csv", encoding='utf-8') as views, open("analysis.csv", "w", newline='', encoding='utf-8') as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        
        for row in reader:
            row["brightness"] = round(calc_brightness(f"{row['id']}.jpg"), 2)
            writer.writerow(row)
            # print(round(brightness, 2))
            # writer.writerow(
            #     {
            #         "id": row["id"],
            #         "english_title": row["english_title"],
            #         "japanese_title": row["japanese_title"],
            #         "brightness": round(brightness, 2)
            #     }
            # )
            

def calc_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L")))/255
    return brightness


main()