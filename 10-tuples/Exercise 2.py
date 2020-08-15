fileName = input('Please enter a file name:')

try:
    file = open(fileName)

except:
    print('Please enter a valid file name, next time')
    exit()

timeCountDict = dict()

for line in file :
    if line.startswith('From'):
        wordsInline = line.split()
        if len(wordsInline) >= 3:
            timeOfSending = int(wordsInline[5].split(':')[0])
            timeCountDict[timeOfSending] = timeCountDict.get(timeOfSending, 0) + 1

timesCountList = list(timeCountDict.items())
timesCountList.sort()

for time , count in timesCountList:
    if time < 10 :
        print("0"+ str(time), count)
    else:
        print(time, count)
