import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## my code:

url = input("Enter location:")
print('Retrieving', url)


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieving',len(data),'characters')
tree = ET.fromstring(data)
## now we have pulled in the data


##finding the total number of users or 'names' and the sum of their id or 'count'
lst1=tree.findall('comments/comment')
sum_total=0
print('Count:',len(lst1))
for item in lst1:
    num=item.find('count').text
    numb=int(num)
    sum_total=sum_total+numb
print('Sum:',sum_total)










#
