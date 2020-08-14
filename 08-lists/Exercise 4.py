fileName = input("Enter file:")

try :
    file = open(fileName)
except :
    print("Wrong file name, please enter a correct one")
    exit()


listOfWords = []

for line in file :
    listWordsPerLine = line.split()
    for word in listWordsPerLine:
        if not listOfWords.count(word): listOfWords.append(word)

listOfWords.sort()
print(listOfWords)

