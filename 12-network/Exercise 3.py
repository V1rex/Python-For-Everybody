import urllib.request, urllib.parse, urllib.error

pageURL = input("Enter -")
content = urllib.request.urlopen(pageURL).read().decode().strip()
count = 0
print(content)

for char in content :
    if count <= 3000 :
        print(char, end='')

    count = count + 1

print("\n\nThe number of characters in this page is : " + str(count))