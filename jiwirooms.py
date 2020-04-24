import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
city=input()
checkin=input()
checkout=input()
city=city.lower()
myurl=f"https://jiwirooms.com/search-hotel?city={city}&checkin={checkin}&checkout={checkout}&adult=1&children=0&nors=1"
uClient=uReq(myurl)
page_soup=soup(uClient,'html.parser')
containers=page_soup.find_all("div",{"col-lg-12 hotel p-3"})
for x in containers:
    d=x.find('a',{"jiwi_link_black"})
    BOOK='https://jiwirooms.com'+d['href']
    f=x.find('span',{"hotel-name capitalize"})
    c=f.find('a',{"jiwi_link_black capitalize"})
    name=c.text
    img=d.find('img',{"hotel_list_image w-100"})
    image=img['src']
    addre=x.find('address',{"capitalize"})
    price_1=x.find('div',{"col-lg-4 cost text-center"})
    
    print(price_1)
    y=x.find_all("i",{'fa fa-star active'})
    Rating=len(y)
    loc=addre.text
    location=loc.split(',')
    location=location[0]
    h=name+","+location+","+image+","+str(Rating)+","+BOOK
#     with open('jiwirooms.csv','w') as f:
#         f.write(h)