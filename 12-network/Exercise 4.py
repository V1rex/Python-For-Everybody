import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import  ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup('p')
count = 0
for paragraph in paragraphs:
    count += 1

print("The number of paragraph in this page is : " + str(count))