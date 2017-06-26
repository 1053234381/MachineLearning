from math import log


def calcShannonEnt(dataSet):
    labels = {}
    num = len(dataSet)
    for data in dataSet:
        label = data[-1]
        if label not in labels.keys():
            labels[label] = 0
            labels[label] += 1
        else:
            labels[label] += 1
    shannonEnt = 0.0
    for key in labels:
        prob = float(labels[key]) / num
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, index, value):
    retDataSet = []
    for data in dataSet:
        temp = []
        if data[index] == value:
            temp = data[:index]
            temp.extend(data[index + 1:])
        retDataSet.append(temp)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFratures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoEntropy = 0.0
    bestFeat = -1
    for i in range(numFratures):
        featureValues = [data[i] for data in dataSet]
        featureValues = set(featureValues)
        newEntropy = 0.0
        for featureValue in featureValues:
            subDataSet = splitDataSet(dataSet, i, featureValue)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoEntropy = baseEntropy - newEntropy
        if infoEntropy > bestInfoEntropy:
            bestInfoEntropy = infoEntropy
            bestFeat = i
    return bestFeat
