fileName = input("Enter a file name :")

try:
    fileContent = open(fileName)
except:
    print("Please type a valid file name ")
    exit()

wordsCount = dict()

for line in fileContent:
    if line.startswith("From"):
        listOfWordsInLine = line.split()
        if len(listOfWordsInLine) >= 3 :
            day = listOfWordsInLine[2]
            wordsCount[day] = wordsCount.get(day, 0) + 1

    else: continue


print(wordsCount)



