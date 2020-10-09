def no_dups(string):
    tempStore = {}
    splitString = string.split()
    result = ""

    for i in range(len(splitString)):
        if splitString[i] not in tempStore.values():
            tempStore[i] = splitString[i]

    for i in tempStore:
        if not i:
            result = result + tempStore[i]
        else:
            result = result + " " + tempStore[i]
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
