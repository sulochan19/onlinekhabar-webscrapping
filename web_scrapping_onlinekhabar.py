import csv
from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.onlinekhabar.com/').text

soup=BeautifulSoup(source,'html.parser')


total_content=soup.find('ul',class_='trending')
# print(total_content.prettify())

for topic in total_content.find_all('li'):
    #print(topic.prettify())
    title=topic.a.text
    link=topic.a['href']
    print(link)
    # print(title)



