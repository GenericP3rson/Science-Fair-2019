from PIL import Image
import os
path = "harvard/full_set"
total = len(os.listdir(path))
i = 0
x = 150
for filename in os.listdir(path):
    if (filename != ".DS_Store"):
        image = Image.open("harvard/full_set/" + filename)
        image = image.resize((x, x))
        image.save("harvard/mini_set/" + filename, "JPEG", optimize=True)
        print(filename + ": " + str(i) + "/" + str(total))
    i+=1

print(len(os.listdir("harvard/mini_set")))