
# Sting expressions :

'spam eggs'  # single quotes, result : spam eggs



'doesn\'t'  # use \' to escape the single quote, result : doesn't



"doesn't"  # ...or use double quotes instead gives the same result as the last one



s = 'First line.\nSecond line.'  # \n means newline
'''  result of the last variable: 
First line.
Second line.
'''


print(r'C:\some\name')  # the r in here expresses that the sting is raw, result : C:\some\name






# Multiple lines string with """...""" or '''...'''.

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

''' RESULTS :
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
'''





# Regroup two strings :

concatenated_string = 3 * 'un' + 'ium'   # result : unununium

text = ('Put several strings within parentheses ' 'to have them joined together.')
# reuslt : Put several strings within parentheses to have them joined together.



# Strings have indexes :

word = 'Python'
word[0]  # character in position 0, result = P

word[0:2]  # characters from position 0 (included) to 2 (excluded) result : Py

word[:2]   # character from the beginning to position 2 (excluded) result : Py

word[4:]   # characters from position 4 (included) to the end result : on

'J' + word[1:] # result : Jython




# The length of a string  :

s = 'supercalifragilisticexpialidocious'
len(s) #Return an integer, result : 34