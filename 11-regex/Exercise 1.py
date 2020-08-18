import re

fileName = "mbox.txt"

file = open(fileName)

regEx = input('Enter a regular expression:')
count = 0

for line in file :
    line = line.strip()
    x = re.findall(regEx, line)
    if len(x) > 0 : count = len(x) + count

print(fileName + " " + "had " + str(count) + " line that matched " + regEx )