listOfNumbers = []
while True:
    numberStr = input("Enter a number:")
    try:
        numberFlt = float(numberStr)

    except:
        if numberStr == "done" : break
        else :
            print('Please enter a nummber')
            continue

    listOfNumbers.append(numberFlt)

print("Maximum:", max(listOfNumbers))
print("Minimum:", min(listOfNumbers))
