from datetime import time

import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import mysql.connector
Db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="db_name"
)
con = Db.cursor()
review_title=[]
review_text=[]
sizee=[]
color=[]
verified=[]

for page in range(1, 20):
    html_doc = requests.get(
        "https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5TNJHG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviewss&pageNumber=" + str(page)).text
    soup = BeautifulSoup(html_doc, 'html.parser')#fetching upto 19 pages
    soup.prettify()
    for i in soup.find_all("a", class_="review-title"):
        i=str(i.get_text()).replace("\n", "")#Review Title
        review_title.append(i)
    for i in soup.find_all('span', attrs={'class':"a-size-mini a-color-state a-text-bold"}):
        i=str(i.get_text()).replace('\n',"")#Verified
        verified.append(i)
    for i in soup.find_all("a", attrs={'class':"a-size-mini a-link-normal a-color-secondary"}):
        list_data=str(i.get_text()).replace("Style name: ","").replace("Colour: (PRODUCT)"," ").replace("Colour:"," ").split()
        sizee.append(list_data[0])#size
        color.append(list_data[1])#Color
    for j in soup.find_all('div', attrs={'class': 'a-row a-spacing-small review-data'}):
        j=str(j.get_text()).replace("\n","").replace("  ","")
        review_text.append(j)#Review_text


output=[]

for i,j,h,k,l in zip(review_title,review_text,sizee,color,verified):
    data={}
    data["review_title"]=i
    data["review_text"]=j
    data["size"]=h
    data["color"]=k
    data["verified"]=l
    My_Qurie="INSERT INTO Reviews(review_title,review_text,size,color,verified)VALUES(%s, %s, %s, %s, %s)"
    val = (i, j, h, k,l)
    con.execute(My_Qurie, val)
    Db.commit()
    output.append(data)
    time.sleep(2)
print("completed")
# import json
# with open("myfile.json", "w",encoding='utf-8') as data1:
#
#     json.dump(output,data1 ,ensure_ascii=False)







