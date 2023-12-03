dictNums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def readFile():
    file = open("input.txt", "r")
    tabOfCodes = file.read().split("\n")
    return tabOfCodes

def findWordsInString(input):
    tabofNums = []
    for i in input:
        tabOfIndexes = []
        for word in dictNums.keys():
            if word in i:
                index = i.find(word)
                tabOfIndexes.append(index)
        tabofNums.append(sorted(tabOfIndexes))
    return tabofNums

def findFirstAndLastNumber(input):
    firstNumber = ""
    lastNumber = ""
    numberList = []
    for i in input:
        firstNumber = ""
        lastNumber = ""
        for j in i:
            if j.isnumeric() and firstNumber == "":
                firstNumber = j
            elif j.isnumeric() and firstNumber != "":
                lastNumber = j
        if lastNumber == "":
            numberList.append(int(firstNumber + firstNumber))
        else:
            numberList.append(int(firstNumber + lastNumber))

    return numberList



def main():
    tabOfCodes = readFile()
    # numbers = findFirstAndLastNumber(tabOfCodes)
    # sumOfNumbers = sum(numbers)
    # print(sumOfNumbers)
    print(tabOfCodes)
    newTab = findWordsInString(tabOfCodes)
    # newNums = findFirstAndLastNumber(newTab)
    print(newTab)
    # print(newNums)
    # print(sum(newNums))


main()