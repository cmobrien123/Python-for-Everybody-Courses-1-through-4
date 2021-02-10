# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


## these 3 lines "clean up" the source code of a website, the flexability of b4s
url = 'http://www.dr-chuck.com/page1.htm'
# url = input('Enter url here: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')  ##geting all the tages '<a' at the website's source code (this has to be 'a')
for tag in tags:
    print(tag.get('href', None))
