'''
So, step one identifying the body part.
We can take user input to figure out what they are scanning and work from there.
'''
from PIL import Image
def all():
    filename = input("Input the image of the body body you would like to scan. (Note:: Input the COMPLETE PATHWAY and be sure the file is in this folder.) ")
    try:
        image = Image.open(filename)
        # For this, it must be the complete pathway and in the folder
        if (image == None):
            print("error")
        else:
            image.show()
    except:
        print("err")
    body_part = input("What body part are you scanning? (Options:: arm, leg, back, face, torso, foot, hand) ").lower()
    print(body_part)
    # This just inputs whatever the body part is.
    # From here, we can do semantic segmentation to figure out what is what.
    # For the basic parts (e.g. back), we can just blacken out anything that isn't the back. For more complex things (e.g. face), we have to blacken anything that is not skinself.
    # Should I also create something to be able to identify clothing?
    # For everything that is not arm, I'll have to mark it as null
    def ss_arm():
        # Does Semantic segmentation for the arm
        return "Pending"
    if (body_part == "arm"):
        ss_arm()
all()
