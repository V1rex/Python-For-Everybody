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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    print(data.decode())
mysock.close()