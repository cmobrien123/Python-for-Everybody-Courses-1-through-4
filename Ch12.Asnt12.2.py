import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Regean.html'

def jump_to_next(url):
##opening the file and using b4s to pull/clean data
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# making a dictionary of the names and url by, with sequence postion as the key
    name_url= dict()
    name_position=0
    tags = soup('a')
    for tag in tags:
        name_position=name_position+1
        tag=str(tag)
        tag=tag.rstrip()
        name=re.findall('html">(\S+)<',tag)
        link=re.findall('href="(\S+)">',tag)
        name_url[name_position]=link[0],name[0]
    ## pulling out the 3rd link
    next_link_list=str(name_url[18])
    # print(next_link_list)
    current_name=re.findall('html\', \'(\S+)\'',next_link_list)
    next_link_list=re.findall('(http\S+html)',next_link_list)
    next_link=next_link_list[0]
    print(next_link,current_name)
    return(next_link)

##Running the function 7 times
jump_to_next(jump_to_next(jump_to_next(jump_to_next(jump_to_next(jump_to_next(jump_to_next(url)))))))






#
