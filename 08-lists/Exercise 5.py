fileName = input('Enter a file name :')

try :
    file = open(fileName)

except:
    print('Please enter a valid file name')
    exit()

listOfEmails = []


for line in file:
    if line.startswith('From'):
        listOfEmails.append(line.split()[1])

for emails in listOfEmails :
    print (emails)

print(len(listOfEmails))


