import socket

pageURL = input("please type the URL of the page you wanna request :")
print(pageURL.split('/'))

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    mysock.connect((pageURL.split('/')[2], 80))
except:
    print("Plase type a valid web page URL ")
    exit()



cmd = ('GET ' + pageURL +  'HTTP/1.0\r\n\r\n').encode()

print(cmd)

mysock.send(cmd)

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    contentPage = data.decode().strip()

    for char in contentPage :
        if count <= 3000 :
            print(char, end='')
        count = count + 1



print("\nThe number of characters is : " + str(count))
mysock.close()