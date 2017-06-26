import re
from collections import defaultdict


def words(text):
    return re.findall("[a-z]+", text.lower())


def train(features):
    model = defaultdict(lambda: 1)
    for feature in features:
        model[feature] += 1
    return model


NWORDS = train(words(open("big.txt", "r").read()))

alphabet = "abcdefghijklmnopqrstuvwxyz"


def edit1(word):
    splits = split(word)
    deletes = delete(splits)
    transposes = transpose(splits)
    replaces = replace(splits)
    inserts = insert(splits)
    return set(deletes + transposes + replaces + inserts)


def split(word):
    splits = []
    for i in range(len(word) + 1):
        if i == len(word):
            a == word[:i]
            b == ''
            splits.append((a, b))
        else:
            a = word[:i]
            b = word[i:]
            splits.append((a, b))
    return splits


def delete(splits):
    deletes = []
    for a, b in splits:
        if b == '':
            deletes.append(a[:-1])
        elif len(b) == 1:
            deletes.append(a)
        else:
            deletes.append(a + b[1:])
    return deletes


def transpose(splits):
    transposes = []
    for a, b in splits:
        if len(b) == 2:
            transposes.append(a + b[1] + b[0])
        elif len(b) > 2:
            transposes.append(a + b[1] + b[0] + b[2:])
        else:
            continue
    return transposes


def replace(splits):
    replaces = []
    for a, b in splits:
        if len(b) == 0:
            for c in alphabet:
                replaces.append(a[:-1] + c)
        elif len(b) == 1:
            for c in alphabet:
                replaces.append(a + c)
        else:
            for c in alphabet:
                replaces.append(a + c + b[1:])
    return replaces


def insert(splits):
    inserts = []
    for a, b in splits:
        for c in alphabet:
            inserts.append(a + c + b)
    return inserts


def known_edit2(word):
    return set(e2 for e1 in edit1(word) for e2 in edit1(e1) if e2 in NWORDS)


def known(words):
    return set(word for word in words if word in NWORDS)


def correct(word):
    candidates = known([word]) or known(edit1(word)) or known_edit2(word) or [word]
    return max(candidates, key=NWORDS.get)


if __name__ == "__main__":
    while True:
        word = input("please input a word\n")
        print("the correct word is %s" % (correct(word)))
