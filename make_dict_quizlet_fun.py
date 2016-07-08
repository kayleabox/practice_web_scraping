from lxml import html
from lxml import etree
import requests

def webscraping_dict(webpage, xpath_one, xpath_two):

    rus_list = webscraping_list(webpage, xpath_one)
    eng_list = webscraping_list(webpage, xpath_two)
    word_dict = {}

    print(rus_list)
    print (eng_list)

    index=0
    for item in rus_list:
        print(rus_list[index])
        print (eng_list[index])
        word_dict[rus_list[index]] = {eng_list[index]}
        index+=1

    #print (word_dict)
    return word_dict

def webscraping_list(webpage, x_path):
    page = requests.get(webpage)
    tree = html.fromstring(page.content)

    list= tree.xpath(x_path)
    return list