import pandas as pd 
import random

dataset = pd.read_csv("harvard/HAM10000_metadata.csv")

key = [
    ["akiec", [1, 0, 0, 0, 0, 0, 0]],
    ["bcc", [0, 1, 0, 0, 0, 0, 0]],
    ["bkl", [0, 0, 1, 0, 0, 0, 0]],
    ["df", [0, 0, 0, 1, 0, 0, 0]],
    ["mel", [0, 0, 0, 0, 1, 0, 0]],
    ["nv", [0, 0, 0, 0, 0, 1, 0]],
    ["vasc", [0, 0, 0, 0, 0, 0, 1]]
]  # This is the key

def open_and_random(dataset):
    '''
    This will open a CSV, split it into two sections, mix it, then turn it back into a DataFrame.
    '''
    dataset = pd.read_csv(dataset)  # Opens the dataset
    dataset = [dataset.iloc[i] for i in range(len(dataset))]
    # print(dataset)
    # random.shuffle(dataset)  # Shuffles the dataset
    canc = [["akiec", []], ["bcc", []], ["bkl", []], ["df", []], ["mel", []], ["nv", []], ["vasc", []]]
    for row in dataset: # Looks at each point in dataset
        for dis in canc: # Looks at each disease in the cancer
            if (row[2] == dis[0]): # If the row's cancer is the cancer in the dataset, append to canc.
                dis[1].append([row[1], row[2]]) # Just adding the image and cancer, 'cause that's all we need
                break
    print(canc) 
    # Now that they are separated, we should partition the data.
    all_test = []
    all_train = []
    for data in canc:
        l = round(len(data[1])/2)
        train_data = data[1][:l] # Splits the two roughly in half
        test_data = data[1][l:]
        data.append(train_data)
        data.append(test_data) # Adds it into the canc list
        all_test +=test_data
        all_train += train_data
    # print(canc)
    # print(len(canc[0]))
    random.shuffle(all_test) 
    random.shuffle(all_train) # Mixing the two datasets
    test_data = [i[0] for i in all_test] # Adds all the testing data
    test_labels = [i[1] for i in all_test] # Adds all the labels
    train_data = [i[0] for i in all_train]
    train_labels = [i[1] for i in all_train]
    traindf = pd.DataFrame({"image_id": train_data})
    traindf["dx"] = train_labels
    testdf = pd.DataFrame({"image_id": test_data})
    testdf["dx"] = test_labels
    # print(testdf, traindf)
    print(traindf)
    return [traindf, testdf]

train, test = open_and_random("harvard/HAM10000_metadata.csv")


# def test():
#     li = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
#     li1 = li[:round(len(li)/2)]
#     li2 = li[round(len(li)/2):]
#     print(li1)
#     print(li2)
# test()
