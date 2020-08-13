

fileName = input("Enter a file name: ")
try:
    file = open(fileName)
    filecontentUpperCase = file.read().upper()
    print(filecontentUpperCase)
    print("The operation is done succesfully !")

except:
    print("Please try again typing a valid file name")



