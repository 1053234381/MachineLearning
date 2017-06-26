import numpy as np
import operator


def classfy(x, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(x, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDist = sqDiffMat.sum(axis=1)
    dist = sqDist ** 0.5
    sortedDistIndicies = np.argsort(dist)
    countLabels = {}
    for i in range(k):
        label = labels[sortedDistIndicies[i]]
        countLabels[label] = countLabels.get(label, 0) + 1
    sortedCountLabels = sorted(countLabels.items(), key=operator.itemgetter(1), reverse=True)
    return sortedCountLabels[0][0]


def fileToMat(filename):
    fr = open(filename)
    lines = fr.readlines()
    print(lines)
    dataSet = np.zeros((len(lines), 3))
    labels = []
    index = 0
    for line in lines:
        line = line.replace("\n", "")
        listOfLine = line.split("\t")
        for i in range(len(listOfLine) - 1):
            dataSet[index, i] = float(listOfLine[i])
        labels.append(listOfLine[-1])
        index += 1
    print(dataSet)
    return dataSet, labels


# def normalize(dataSet):


dataSet, labels = fileToMat("datingTestSet2.txt")
result = classfy([38344, 1.669788, 0.134296], dataSet, labels, 50)
print(result)
