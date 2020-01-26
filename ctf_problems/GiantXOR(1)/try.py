import sys


def frequencyAnalyse(string):
    charList = []
    frequencyList = []

    temp = string.replace(" ", "")
    stringList = list(temp)

    for i in xrange(len(stringList)):
        if stringList[i] in charList:
            for j in xrange(len(charList)):
                if stringList[i] == charList[j] and i != j:
                    frequencyList[j] += 1
        else:
            charList.append(stringList[i])
            frequencyList.append(1)
    return charList, frequencyList

def indexofCoincidence(StringInp):
    for keyLength in xrange(1, 100):
        matchCount = 0
        totalCount = 0
        for i in range(len(StringInp)):
            for j in range(i+keyLength, len(StringInp), keyLength):
                totalCount += 1
                if StringInp[i] == StringInp[j]:
                    matchCount += 1
        ioc = float(matchCount) / float(totalCount)
        print "Keylength:", keyLength, "   Index of Coincidence(%):", ioc*100


if __name__ == '__main__':
    stringInput = raw_input("Enter the ciphertext to be analysed, in hex: ")
    stringInput = stringInput.decode("hex")
    indexofCoincidence(stringInput)