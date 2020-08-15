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
        if len(wordsInLine) >= 3:
            emailsCount[wordsInLine[1]] = emailsCount.get(wordsInLine[1],0) + 1

listOfEmailsCount = list()
for email, counts in emailsCount.items():
    listOfEmailsCount.append( (counts, email) )

listOfEmailsCount.sort(reverse=True)

mostCountedEmail = listOfEmailsCount[0]
print(mostCountedEmail[1], mostCountedEmail[0])
