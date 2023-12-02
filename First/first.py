def readFile():
    file = open("input.txt", "r")
    tabOfCodes = file.read().split("\n")
    return tabOfCodes

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
    numbers = findFirstAndLastNumber(tabOfCodes)
    print(sum(numbers))

main()