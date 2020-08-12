numberOfHours = float(input('Enter Hours:'))

rateNumber = float(input('Enter Rate:'))

if numberOfHours > 40 :
    pay = numberOfHours * rateNumber * 1.5

else :
    pay = numberOfHours * rateNumber

print('Pay : ', pay , '$')