import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_902131.xml"
html = urllib.request.urlopen(url, context=ctx).read()


print("Retriving",url)
tree=ET.fromstring(html)

counts=tree.findall('.//count')



