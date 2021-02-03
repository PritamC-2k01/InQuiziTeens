import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET

import json
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_902132.json"
html = urllib.request.urlopen(url, context=ctx).read()


print("Retriving",url)
#tree=ET.fromstring(html)
doc=json.loads(html)
#print(doc['comments'])
info=doc['comments']
##info=re.findall('comments',doc)
print("Retrieved",url)
add=0
for cmnt in info:
    num=cmnt['count']
    add+=int(num)
print(add)
