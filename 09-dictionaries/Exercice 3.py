fileName = input("Enter a file name :")

try:
    fileContent =  open(fileName)
except:
    print("Please enter a valid file name ")
    exit()

emailsCount = dict()

for line in fileContent:
    if line.startswith("From"):
        wordsInLine = line.split()
        if len(wordsInLine) >= 3: emailsCount[wordsInLine[1]] = emailsCount.get(wordsInLine[1],0) + 1

print(emailsCount)