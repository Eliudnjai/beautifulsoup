import requests
from bs4 import BeautifulSoup

request=requests.get("https://www.johnlewis.com/john-lewis-bala-pre-lit-potted-fir-christmas-tree-7ft/p2603419")
content=request.content
soup=BeautifulSoup(content,"html.parser")
element=soup.find("span",{"itemprop":"price","class":"now-price"})

string_price=element.text.strip()

price_without_symbol=string_price[1:];

print(float(price_without_symbol)) 

wanted_price=50;

if float(price_without_symbol) <= wanted_price:
    print("buy it")
else:
    print("don't")