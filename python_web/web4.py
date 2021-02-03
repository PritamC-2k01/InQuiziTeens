from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Maryk.html"
i=0
while i<=6:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    lines= soup('a')


    url=lines[17].get('href',None)
    i+=1
    print("turn",i)
    if i<7:
        continue
    else:
        print(url)
    
