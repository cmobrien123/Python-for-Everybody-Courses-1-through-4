

##3 ch13 Using web services

##13.1 eXtensible Markup Language - XML
# #best used for sending documents

# XML looks very similar to HTML, but XML is more structured than HTML. Here is a sample of an XML document:
# <person> <name>Chuck</name> <phone type="intl">
#     +1 734 303 4456
# </phone>
# <email hide="yes" /> </person>

#good idea to think of XML as a tree structure

import xml.etree.ElementTree as ET   ## need to pull in to work with XML

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''  #serialization. This is genunely just a colection of text in an agreed upon format. ### when it gets to the other side, it is de-serialized


tree = ET.fromstring(data)  ## this is creating the tree we were making before (if bad XML, this blows up :-(  )
print('Name:', tree.find('name').text) ## find the tag name as text
print('Attr:', tree.find('email').get('hide'))  ## this is getting the atribute (there is not text)
### tip: try to do these branch by branch (can get pretty long for a single line of code)

### writing loops through nodes

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''  ## that these is a /at the ending tag for each node
## note that the x="7" attribute  is part of the second user branch and is a different branch than <id> or <name>
## the parts with a = in them are attributes
## there is always one outmost tag (<stuff>)
## /> is a self closing tag (don't need the </tag>)
## note that the "" need to be used vs the ''

stuff = ET.fromstring(input)  #### again, stuff is the tree (we usually want to do this)
lst = stuff.findall('users/user') ##note that similar to b4s, we can use the findall() function for xml. need to use findall since many
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
## is seen in the example below, you need to include all of the parent or "closer to the trunk" nodes or nothing gets returned (don't need the outer most tho)

stuff= ET.fromstring(input)

lst=stuff.findall('users/user') ##note that you do not need 'stuff, that will actually mess this up'
print('user count:',len(lst))

lst2=stuff.findall('user')
print('user count:',len(lst2))

### XML Schema

## act of verify the data is in format that is acceptable. Like a contract
## formatting similar to XLM (is a form of XML) that outlines expected format (ex.  name of tags)

## XML is really its own topic and would be better suited within its own seperate course :) but imporant understand the basic idea



##13.4 JavaScript Object Notation - JSON

## it is in general simplier with lower capability. However, it is able to to map DIRECTLY to a some list/dictionary
## becoming the prefered method

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''#straightforward as a dictionary (not a tree)
## no attritbutes
## no outermost 'branch'

info = json.loads(data)##different commands than above. Since already a dictionary, no need for the findall() (dictionaries inside of dictionary)
print('User count:', len(info))

for item in info:
    print('Name', item['name']) ## nice easy syntax :-)
    print('Id', item['id'])
    print('Attribute', item['x'])


import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["phone"]["number"])  ##syntax for getting dictionary within a dictionary







### 13.6 Application Programming Interfaces
# A SOA approach is one where our overall application makes use of the services of other applications.
# A non-SOA approach is where the application is a single standalone application which contains all of the code necessary to implement the application.
## the API is basically the "rules" of a web service that the other applications must follow in order to interact with it


#(1) we always maintain only one copy of data (this is particularly important for things like hotel reservations where we do not want to over-commit) and
#(2) the owners of the data can set the rules about the use of their data.

##13.7 Security and API usage

## often you need a key to acess an API in order to look at data



## twitter ex. NOTE to run this you would need an account

# import urllib
# import twurl
#
# TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
#
#
# ###
# while True:
#     print ''
#     acct = raw_input('Enter Twitter Account:')
#     if ( len(acct) < 1 ) : break
#     url = twurl.augment(TWITTER_URL,
#         {'screen_name': acct, 'count': '2'} )
#     print 'Retrieving', url
#     connection = urllib.urlopen(url)
#     data = connection.read()
#     print data[:250]
#     headers = connection.info().dict
#     # print headers
#     print 'Remaining', headers['x-rate-limit-remaining']
#
#
#
# ## mas twitter
# import urllib
# import twurl
# import json
#
# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
#
# while True:
#     print ''
#     acct = raw_input('Enter Twitter Account:')
#     if ( len(acct) < 1 ) : break
#     url = twurl.augment(TWITTER_URL,
#         {'screen_name': acct, 'count': '5'} )
#     print 'Retrieving', url
#     connection = urllib.urlopen(url)
#     data = connection.read()
#     headers = connection.info().dict
#     print 'Remaining', headers['x-rate-limit-remaining']
#     js = json.loads(data)
#     print json.dumps(js, indent=4)
#
#     for u in js['users'] :
#         print u['screen_name']
#         s = u['status']['text']
#         print '  ',s[:50]







##the below code is out of date I think (runs an infinent loop)

# import urllib
# import urllib.request, urllib.parse, urllib.error
# import json
#
# # serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'
#
# while True:
#     # address = input('Enter location ')
#     address = ('Ann Arbor, MI')
#     if len(address) < 1 : break
#
#     url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
#     print ('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print ('Retrieved',len(data),'characters')
#
#     try: js = json.loads(str(data))
#     except: js = None
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print ('==== Failure To Retrieve ====')
#         print (data)
#         continue
#
#     print (json.dumps(js, indent=4))
#
#     lat = js["results"][0]["geometry"]["location"]["lat"]
#     lng = js["results"][0]["geometry"]["location"]["lng"]
#     print ('lat',lat,'lng',lng)
#     location = js['results'][0]['formatted_address']
#     print (location)



### another example




#
