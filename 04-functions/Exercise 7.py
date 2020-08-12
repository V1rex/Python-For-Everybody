def computegrade (score) :
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print("Your Grade is : A")

        elif score >= 0.8:
            print("Your Grade is : B")

        elif score >= 0.7:
            print("Your Grade is : C")

        elif score >= 0.6:
            print("Your Grade is : D")

        elif score < 0.6:
            print("Your Grade is : F")

    else:
        print("please type a correct score")

print("Welcome to the score to grade converter program")

try:
    studentScore = float(input('Please type in your score: '))
except :
    print("Try again, you did not type a number")
    exit() # the program exit if the input is not a float

computegrade(studentScore)