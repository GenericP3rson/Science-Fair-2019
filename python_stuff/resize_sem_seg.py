from PIL import Image
import os
path = "harvard/full_set"
total = len(os.listdir(path))
i = 0
x = 150
new_path = "Face_Dataset.1"
paths = []
for path in paths:
    for filename in os.listdir(path):
        if (filename != ".DS_Store"):
            image = Image.open(path + "/" + filename)
            image = image.resize((x, x))
            image.save(new_path + "/" + filename, "JPEG", optimize=True)
            print(filename + ": " + str(i) + "/" + str(total))
        i += 1

print(len(os.listdir("harvard/mini_set")))
