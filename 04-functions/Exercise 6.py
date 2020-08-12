
def computepay(hours , rate):
    if hours > 40:
        pay = hours * (rate * 1.5)

    else:
        pay = hours * rate

    print('Pay : ', pay, '$')


try:
    numberOfHours = float(input('Enter Hours:'))
    rateNumber = float(input('Enter Rate:'))

except :
    print("please enter number")
    quit()

computepay(numberOfHours, rateNumber)






