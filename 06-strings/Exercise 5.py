
str = 'X-DSPAM-Confidence : 0.8475 '
print(str)
indexOfColon = str.find(':')

numberStr = str[indexOfColon+1:].strip()

number = float(numberStr)
print(number)

