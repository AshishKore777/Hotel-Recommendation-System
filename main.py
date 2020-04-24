from flask import Flask, render_template, url_for,request
import pandas as pd
import os


app = Flask(__name__)

l=list()
a=pd.read_csv("final1.csv")
for i in range(0,len(a)):
    l.append(a.values[i])


@app.route('/',methods=["POST","GET"])
def f1():
    if request.method=="POST":
        ci=request.form.get("mycity")
        chin=request.form.get("chin")
        chout=request.form.get("chout")
        
        
        return render_template("test.html",len = len(l),l=l,chin=chin,chout=chout)
    return render_template('frontpage.html')
#         ci=request.form.get("mycity")


#         import re
#         import os,csv
#         import pandas as pd
#         from bs4 import BeautifulSoup as soup
#         from urllib.request import urlopen as uReq
#         c=0

#         # os.remove('final.csv')

#         def mstay(city,checkin):
#             SITE='MISTAY'
#             city = city.lower()
#             myurl = f"https://www.mistay.in/hotels-in-{city}/?checkin_date={checkin}&checkin_slot=1&slot_count=6&guest_count=2&room_count=1"
#             uClient = uReq(myurl)
#             page_soup = soup(uClient, 'html.parser')
#             containers = page_soup.find_all("div", {"content"})
#             link = page_soup.find_all("img", {"class": "lazy"})
#             t = len(link)
#             rating = page_soup.find_all('input', {"class": "star-rating"})
#             j=0
#             for i in range(12, 12 + t):
#                 name = containers[i].find("div", {"class": "hotel-name overflow-ellipsis"})
#                 location = containers[i].find("div", {"class": "hotel-location overflow-ellipsis"})
#                 price = containers[i].find("div", {"class": "pricing"})
#                 a, b, c = name.text, location.text, price.text
#                 r = a.split()
#                 v = ''
#                 for z in r:
#                     z = z.lower()
#                     v = v + '-' + z
#                     v = v[1:]
#                 BOOK = f"https://www.mistay.in/hotels-in-{city}/{v}/?checkin_slot=1&checkin_date={checkin}&guest_count=2&slot_count=6&room_count=1"
#                 a = a.strip()
#                 Hotel_Name = a.split(',')
#                 b = b.strip()
#                 b_1=b.split()
#                 c = c.strip()
#                 k = re.findall(r'[0-9]*', c)
#                 m = 0
#                 g = ''
#                 d = ''
#                 for i in k:
#                     if (i != '' and m < 7):
#                         g = g + i
#                     elif (i != ''):
#                         d = d + i
#                     else:
#                         m = m + 1
#                 l = link[j]
#                 image = l['data-src']
#                 f = rating[j]
#                 star = f['data-value']
#                 if (g == '' and d == ''):
#                     h=Hotel_Name[0]+","+ b_1[0]+","+"SOLD OUT"+","+ image+","+ star+","+BOOK+","+SITE
#                     if(j==0):
#                         with open('mistay.csv','w') as f:
#                         # f.write('NAME'+','+'LOCATION'+','+ 'PRICE'+','+ 'IMAGE'+','+ 'RATING'+','+'BOOK NOW'+','+'SITE')
#                             f.write("\n")
#                             f.write(h)
#                             f.write("\n")
#                     else:
#                         with open('mistay.csv','a') as f:
#                             f.write(h)
#                             f.write("\n")
#                 else:
#                     h=Hotel_Name[0]+","+b_1[0]+","+d+","+image+","+ star+","+ BOOK+","+SITE
#                     if(j==0):
#                         with open('mistay.csv','w') as f:
#                             print(1245)
#                         # f.write('NAME'+','+'LOCATION'+','+ 'PRICE'+','+ 'IMAGE'+','+ 'RATING'+','+ 'BOOK NOW'+','+'SITE')
#                             f.write("\n")
#                             f.write(h)
#                             f.write("\n")
#                     else:
#                         with open('mistay.csv','a') as f:
#                             f.write(h)
#                             f.write("\n")
#                 print(12345)   
#                 j=j+1
#         def jiwi_rooms(city,checkin,checkout):
#             SITE='JIWIROOMS'
#             city = city.lower()
#             myurl = f"https://jiwirooms.com/search-hotel?city={city}&checkin={checkin}&checkout={checkout}&adult=1&children=0&nors=1"
#             uClient = uReq(myurl)
#             page_soup = soup(uClient, 'html.parser')
#             containers = page_soup.find_all("div", {"col-lg-12 hotel p-3"})
#             j = 0
#             for x in containers:
#                 d = x.find('a', {"jiwi_link_black"})
#                 BOOK = 'https://jiwirooms.com/' + d['href']
#                 f = x.find('span', {"hotel-name capitalize"})
#                 c = f.find('a', {"jiwi_link_black capitalize"})
#                 name = c.text
#                 img = d.find('img', {"hotel_list_image w-100"})
#                 image = img['src']
#                 addre = x.find('address', {"capitalize"})
#                 price_1 = x.find('div', {"col-lg-4 cost text-center"})
#                 price = (re.findall(r'[0-9]{3,4}', str(price_1)))
#                 y = x.find_all("i", {'fa fa-star active'})
#                 Rating = len(y)
#                 loc = addre.text
#                 location = loc.split(',')
#                 locate = re.findall(r'[a-zA-Z]*', location[0])
#                 for x in locate:
#                     if (x != ''):
#                         l = x
#                         break
#                 h=name+","+l+","+ price[0]+","+ image+","+str(Rating)+","+BOOK+","+SITE+check
#                 if(j==0):
#                     with open('jiwirooms.csv','w') as f:
#                         #f.write('NAME'+','+'LOCATION'+','+ 'PRICE'+','+ 'IMAGE'+','+'RATING'+','+ 'BOOK NOW'+','+'SITE'+"\n")
#                         f.write(h)
#                 else:
#                     with open('jiwirooms.csv','a') as f:
#                         f.write(h)
#                         f.write("\n")
#                 j = j + 1
#         city=ci
#         checkin=chin
#         checkout=chout
#         f=checkin.split('-')
#         checkin2=f[2]+'-'+f[1]+'-'+f[0]
#         z=0
#         try:
#             mstay(city,checkin2)
#             c=1
#             jiwi_rooms(city,checkin,checkout)
#             c=2
#         except:
#             if(c==1):
#                 z=1
#             elif(c==2):
#                 z=2
#             elif(c==0):
#                 try:
#                     jiwi_rooms(city,checkin,checkout)
#                     z=3
#                 except:
#                     z=4
#         #COMPARISON
#         if(z==4):
#             print("We have no hotels in this city")
#         elif(z==1):
#             os.rename('mistay.csv','final.csv')
#         elif(c==2):
#             f1=open('mistay.csv','r')
#             f2=open('jiwirooms.csv','r')
#             f3=open('final.csv','w')
#             s1=csv.reader(f1)
#             s2=csv.reader(f2)
#             f3.write('NAME'+','+'LOCATION'+','+ 'PRICE'+','+ 'IMAGE'+','+'RATING'+','+ 'BOOK NOW'+','+'SITE')
#             f3.write("\n")
#             for i in s2:
#                 flag1=0
#                 for j in s1:
#                     flag2=0
#                     if(i!=[] and j!=[]):
#                         if(i[0]==j[0] and i[1]==j[1]):
#                             if i[2]!='SOLD OUT': 
#                                 if int(i[2])<int(j[2]):
#                                     f3.write(i[0]+","+i[1]+","+i[2]+","+i[3]+","+i[4]+","+i[5]+","+i[6])
#                                     f3.write("\n")
#                                     flag1=1
#                                     break
#                                 elif int(i[2])>int(j[2]):
#                                     f3.write(j[0]+","+j[1]+","+j[2]+","+j[3]+","+j[4]+","+j[5]+","+j[6])
#                                     f3.write("\n")
                                    
#                                     flag2=1
#                                     break        
#                 if(flag1==0 and i!=[]):
#                     f3.write(i[0]+","+i[1]+","+i[2]+","+i[3]+","+i[4]+","+i[5]+","+i[6])
#                     f3.write("\n")
#             f1.close()
#             f2.close()
#             f3.close()
#             # os.remove('jiwirooms.csv')
#             # os.remove('mistay.csv')
#         elif(z==3):
#             os.rename('jiwirooms.csv','final.csv')
        
#         return render_template("test.html",len = len(l),l=l,chin=chin,chout=chout)
#     return render_template('frontpage.html')
if __name__ == '__main__':
    app.run(debug=True)
