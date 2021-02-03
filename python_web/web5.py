import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.mapbox.com/geocoding/v5/mapbox.places/87.8549755,22.9867569.json?access_token=pk.eyJ1IjoicHJpdGFtYzAxMiIsImEiOiJja2duZzV6OHIwdm80MnpvNmtkaHQzMDB1In0.KbjzB6vMA4LQ8pMSZrDQhA"
html = urllib.request.urlopen(url, context=ctx).read()


print("Retriving",url)
tree=ET.fromstring(html)

names=tree.findall('.//name')
counts=tree.findall('.//count')

add=0
for i in range(len(names)):
    num1=names[i].text
    num2=counts[i].text
    print(num1,num2)
    
print("Retrieved data")

    
