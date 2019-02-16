# resize_sem_seg.py
from PIL import Image
import os
# path = "Face_Dataset/Pratheepan_Dataset/FacePhoto"
path = "Face_Dataset/Ground_Truth/GroundT_FacePhoto"
total = len(os.listdir(path))
i = 0
x = 750
y = 500
# new_path = "Face_Dataset.1/FacePhoto/Real"
new_path = "Face_Dataset.1/FacePhoto/BW"
paths = []
# for path in paths:
for filename in os.listdir(path):
    if (filename != ".DS_Store"):
        image = Image.open(path + "/" + filename)
        image = image.resize((x, y))
        image = image.convert("RGB")
        image.save(new_path + "/" + filename, "JPEG", optimize=True)
        print(filename + ": " + str(i) + "/" + str(total))
    i += 1

print(len(os.listdir(new_path)))
