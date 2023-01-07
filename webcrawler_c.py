# Program: web crawler
# Download requests module and bs4 module by pip3
# Reference:
# https://ithelp.ithome.com.tw/articles/10202121?sc=hot
# https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/
# https://www.w3schools.com/python/module_requests.asp // requests w3
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/   // BeautifulSoup.doc
# ------------------------ #

import requests
import json
from bs4 import BeautifulSoup  # import BeautifulSoup

# ------------------------ #

x = requests.get(
    "https://e-tutor.itsa.org.tw/e-Tutor/mod/programming/view.php?id=63636")
# requests syntax: requests.methodname(params)
# type(x) class: requests.models.Response
# x.text return str of entire web html

soup = BeautifulSoup(x.text, "html.parser")
# create BeautifulSoup object using "html.parser" by entire web html
# type(soup) class: bs4.BeautifulSoup
# print(BeautifulSoup object) return all web html
# BeautifulSoup object.prettify() retrun formatted html
# BeautifulSoup object.text return plain text

select_all_element = soup.select("div.tab-content ul li a div.tabpanel_title")
# filter required html
# type(select_all_element) class: bs4.element.ResultSet
# Can use bs4.element.ResultSet[int] return sub html

answer = list()

for i in select_all_element:
    # iter all element and file handling put into answer arr
    context = i.text.strip(" ").split(" ", 1)
    context_finish = context[len(context)-1].strip('\n')
    answer.append(context_finish)

# print(answer)
with open("py_result.json", "w", encoding='utf-8') as f:
    # encoding: encoding format
    json.dump(answer, f, indent=4, ensure_ascii=False)
