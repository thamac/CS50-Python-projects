from re import match


def checkLuhn(cardNo):

    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


def main():
    test = True

    while test:
        ccNumber = input("Number: ")
        if (match(('^\\d{13}$'), ccNumber) or match(('^\\d{15}$'), ccNumber) or match(('^\\d{16}$'), ccNumber)):
            test = False
        else:
            return print("INVALID")

    firstNum = ord(ccNumber[0]) - ord('0')
    secondNum = ord(ccNumber[1]) - ord('0')

    option = 0

    if firstNum == 4:
        option = firstNum
    elif firstNum == 3:
        option = int(str(firstNum) + str(secondNum))
    elif firstNum == 5:
        option = int(str(firstNum) + str(secondNum))

    if checkLuhn(ccNumber):
        if option == 4:
            print("VISA")
        elif option == 34 or option == 37:
            print("AMEX")
        elif option >= 51 and option <= 55:
            print("MASTERCARD")
        else:
            print("INVALID")

    else:
        print("INVALID")


main()
