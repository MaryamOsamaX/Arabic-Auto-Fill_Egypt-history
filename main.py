import math


# from nltk.collocations import ngrams

# from nltk.tokenize import RegexpTokenizer


def addToDictionary(e, dictionary):
    if e not in dictionary:
        dictionary[e] = 1
    else:
        dictionary[e] += 1


def createDictionary(triGram):
    dic1 = {}
    dic2 = {}
    dic3 = {}
    for (a, b, c) in triGram:
        addToDictionary(a, dic1)
        addToDictionary((a, b), dic2)
        addToDictionary((a, b, c), dic3)
    a, b, c = triGram[len(triGram) - 1]
    addToDictionary(b, dic1)
    addToDictionary(c, dic1)
    addToDictionary((b, c), dic2)
    return dic1, dic2, dic3


def prop(dic1, dic2, dic3, trigram):
    finaldic = {}
    total1 = 0
    total2 = 0
    total3 = 0

    for key, value in dic1.items():
        total1 += value
    total2 = total1 - 1
    total3 = total1 - 2

    for (a, b, c) in trigram:
        finaldic[(a, b, c)] = math.log(dic1[a] / float(total1)) + math.log(
            dic2[(a, b)] / float(total2)) + math.log(dic3[(a, b, c)] / float(total3))
    return finaldic


def fill(word, allprops):
    words = word.split()
    max_value = -10 ** 100
    ans = ""
    for key, value in allprops.items():
        a, b, c = key
        if len(words) == 1:
            if a == words[0] and value > max_value:
                max_value = value
                ans = a + " " + b + " " + c
        elif len(words) == 2:
            if a == words[0] and b == words[1]:
                max_value = value
                ans = a + " " + b + " " + c
                print(ans, ' ', value)
    return ans


def ngram(text, grams):
    model = []
    count = 0
    for token in text[:len(text) - grams + 1]:
        model.append(text[count:count + grams])
        count = count + 1
    return model


if __name__ == '__main__':
    # read file 
    document = ''.join(open("courps.txt", encoding="utf8").readlines())
    # tokenizing
    tokens = document.split()
    trigram = list(ngram(tokens, 3))
    # counting uni  , bi , tri
    uni, bi, tri = createDictionary(trigram)
    all_props = prop(uni, bi, tri, trigram)
    t = input("Enter the test word:")

    x = fill(t, all_props)

    print("The predicted value is: " + x)
