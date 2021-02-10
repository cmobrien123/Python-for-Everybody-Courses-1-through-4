import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location:")
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieving',len(data),'characters')

info = json.loads(data)##different commands than above. Since already a dictionary, no need for the findall() (dictionaries inside of dictionary)
count=0
sum=0
for item in info["comments"]:
    x=item["count"]
    sum=sum+x
    count=count+1
print('Count:',count)
print('Sum:',sum)

print('hello')
