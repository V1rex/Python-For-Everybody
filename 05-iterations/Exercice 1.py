
count = 0
total = 0
average = 0

while True :
    inputUsr = input('Enter a number: ')
    try:
        number = int(inputUsr)
        count = count + 1
        total = total + number
        average = total / count
    except:
        if inputUsr == "done":
            break
        else:
            print("Invalid input")
            continue

print(count, total , average)