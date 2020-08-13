fileName = input("Enter a file name: ")
try:
    file = open(fileName)
except:
    print("Please try again typing a valid file name")
    exit()

count = 0
totalOfNumbers = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        indexOfColon = line.find(":")
        currentNumber = float(line[indexOfColon + 1 :].strip())

        count = count + 1
        totalOfNumbers = currentNumber + totalOfNumbers


print("Average spam confidence: ", totalOfNumbers/count)


