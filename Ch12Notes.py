# Chapter 12


### 12.1 Hypertext Transfer Protocol - HTTP
import socket  #socket has a library

## sockets is a connection that exists for 2 places to communicate and then goes away

### 12.2 The world’s simplest web browser

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) ## 80 is the port. These 3 lines of code prep the connection, no actual data has been sent

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() ## prepare for sending (encoding) This is in bytes
mysock.send(cmd) ## send it

while True:
    data = mysock.recv(512)  ## recieve 512 peices of data at a time
    if len(data) < 1:  ## when recieving 0 bits of data, stop
        break
    print(data.decode(),end='')  ##decode and print data recieved. When decoding, you are making sure that it is the same "counting system" as you are using. decode goes from bytes to unitcode
mysock.close() ### DO THIS!!!!! sockets take up a good amount of resources. both here and the place we are getting the data from

# one major protocol is that you need to send and recieve data as bytes
# reminder of what a byte is:
    # bytes are how a computer can store data, you have to encode and then decode them
    # If you want to store music, you must first encode it using MP3, WAV, etc.
    # If you want to store a picture, you must first encode it using PNG, JPEG, etc.
    # If you want to store text, you must first encode it using ASCII, UTF-8, etc.
#BUT when you run code, you are are using unicode
## 1) start on my laptop as unicode 2)encode() and send as a byte 3) send() via a socket with the network 4) recv() from the socket (still a btype) 5) decode() and go from byte to string

### 12.3 Retrieveing an image over HTTP

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    time.sleep(0.25)   ## time.sleep is a "pause" for .25 seconds, so the program can "get ahead" before we recv() again
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()



print("pp")
### 12.4 Retrieving web pages with urllib

# there is a simplier way!
# treats the internet pages more like an indiviual file
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())



import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts= dict() ## good example of using a dictionary. words are keys and count is the value :-)
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)


### 12.5 Reading binary files using urllib
#ex. getting an image via the internet


import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()


### 12.6 Parsing HTML and scraping the web

#creating a program to search for paterns on webpages

### 12.7 Parsing HTML and scraping the web (using regular expressions)

# # example webpage:
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.htm"> Second Page</a>.
# </p>

#href="http[s]?://.+?" ## you can use this r.e. to find anything with http:// followed by one of more characters, the ? is for greedy


#search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# ignore SSL certification errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())











## EXTRA: ordinals

print(ord('H'))
print(ord('h'))


x = b'abc'
print(type(x))



#
