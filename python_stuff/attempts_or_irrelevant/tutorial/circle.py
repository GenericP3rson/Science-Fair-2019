from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

from matplotlib import style
style.use("ggplot")


def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(1, 10)
    for eachNum in numbersWeHave:
        for furtherNum in numbersWeHave:

            imgFilePath = 'images/numbers/' + \
                str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachPart in imageArray:
        for theParts in eachPart:
			# for the reduce(lambda x, y: x + y, theParts[:3]) / len(theParts[:3])
			# in Python 3, just use: from statistics import mean
			# then do avgNum = mean(theParts[:3])
            avgNum = reduce(lambda x, y: x + y,
                            theParts[:3]) / len(theParts[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x = x + 1
        except Exception as e:
            print(str(e))
            print("Ouch")

    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()


whatNumIsThis('images/zero.png')





# from PIL import Image
# import numpy as np

# import matplotlib.pyplot as plt
# import time
# from collections import Counter


# def whatNumIsThis(filePath):

#     matchedAr = []
#     loadExamps = open('numArEx.txt', 'r').read()
#     loadExamps = loadExamps.split('\n')

#     i = Image.open(filePath)
#     iar = np.array(i)
#     iarl = iar.tolist()

#     inQuestion = str(iarl)

#     for eachExample in loadExamps:
#         try:
#             splitEx = eachExample.split('::')
#             currentNum = splitEx[0]
#             currentAr = splitEx[1]

#             eachPixEx = currentAr.split('],')
#             eachPixInQ = inQuestion.split('],')

#             x = 0

#             while x < len(eachPixEx):
#                 if eachPixEx[x] == eachPixInQ[x]:
#                     matchedAr.append(int(currentNum))

#                 x += 1
#         except Exception as e:
#             print(str(e))

#     print(matchedAr)
#     x = Counter(matchedAr)
#     print(x)
#     print(x[0])


# whatNumIsThis('images/dot.png')

# def threshold(imageArray): # Makes it all black and white
#     balanceAr = []
#     newAr = imageArray
#     from statistics import mean
#     for eachRow in imageArray:
#         for eachPix in eachRow:
#             avgNum = mean(eachPix[:3])
#             balanceAr.append(avgNum)

#     balance = mean(balanceAr)
#     for eachRow in newAr:
#         for eachPix in eachRow:
#             if mean(eachPix[:3]) > balance:
#                 eachPix[0] = 255
#                 eachPix[1] = 255
#                 eachPix[2] = 255
#                 eachPix[3] = 255
#             else:
#                 eachPix[0] = 0
#                 eachPix[1] = 0
#                 eachPix[2] = 0
#                 eachPix[3] = 255
#     return newAr


# def createExamples(): # Makes a new file with the data
#     numberArrayExamples = open('numArEx.txt', 'a')
#     numbersWeHave = range(1, 10)
#     for eachNum in numbersWeHave:
#         #print eachNum
#         for furtherNum in numbersWeHave:
#             # you could also literally add it *.1 and have it create
#             # an actual float, but, since in the end we are going
#             # to use it as a string, this way will work.
#             print(str(eachNum)+'.'+str(furtherNum))
#             imgFilePath = 'images/numbers/' + \
#                 str(eachNum)+'.'+str(furtherNum)+'.png'
#             ei = Image.open(imgFilePath)
#             eiar = np.array(ei)
#             eiarl = str(eiar.tolist())

#             print(eiarl)
#             lineToWrite = str(eachNum)+'::'+eiarl+'\n'
#             numberArrayExamples.write(lineToWrite)

# i = Image.open('images/numbers/0.1.png')
# iar = threshold(np.array(i))
# i2 = Image.open('images/numbers/y0.4.png')
# iar2 = threshold(np.array(i2))
# i3 = Image.open('images/numbers/y0.5.png')
# iar3 = threshold(np.array(i3))
# i4 = Image.open('images/sentdex.png')
# iar4 = threshold(np.array(i4))
# # Opens and array-i-fies it all


# fig = plt.figure()
# ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
# ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
# ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)
# # Plots and scales the data

# ax1.imshow(iar)
# ax2.imshow(iar2)
# ax3.imshow(iar3)
# ax4.imshow(iar4)


# plt.show()






# # from PIL import Image
# # import numpy as np
# # import matplotlib.pyplot as plt # This is Python3, so it should be fine
# # i = Image.open('images/numbers/y0.4.png')

# # iar = np.asarray(i)


# # plt.imshow(iar)
# # print(iar)
# # plt.show()
# # # This pretty much picks out the image an displays it
