from PIL import Image
import os
path2 = "SKIN1"
path = "harvard/full_set"
# new_path = "SKIN1"
new_path = "harvard/mini_set"
total = len(os.listdir(path)) + len(os.listdir(path2))
i = 1
x = 400
for filename in os.listdir(path):
    if (filename != ".DS_Store"):
        image = Image.open(path + "/" + filename)
        # image = image.convert("RGB")
        image = image.resize((x, x))
        image.save(new_path + "/" + filename, "JPEG", optimize=True)
        # image.save(new_path + "/" + filename+".jpg")
        print(filename + ": " + str(i) + "/" + str(total))
    i+=1
for filename in os.listdir(path2):
    if (filename != ".DS_Store"):
        image = Image.open(path2 + "/" + filename)
        image = image.convert("RGB")
        image = image.resize((x, x))
        # image.save(new_path + "/" + filename, "JPEG", optimize=True)
        image.save(new_path + "/" + filename+".jpg")
        print(filename + ": " + str(i) + "/" + str(total))
    i += 1
print(len(os.listdir(new_path)))
