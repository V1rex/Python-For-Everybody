fileName = input("Enter a file name :")

try:
    fileContent =  open(fileName)
except:
    print("Please enter a valid file name ")
    exit()

domainsCount = dict()

for line in fileContent:
    if line.startswith("From"):
        wordsInLine = line.split()
        if len(wordsInLine) >= 3:
            splitedEmail = wordsInLine[1].split('@')
            domainsCount[splitedEmail[1]] = domainsCount.get(splitedEmail[1], 0) + 1

print(domainsCount)