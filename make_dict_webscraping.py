from lxml import html
import requests


def webscraping_dict(webpage, xpath_one, xpath_two, xpath_three):

    altered_list = []
    first_list = webscraping_list(webpage, xpath_one)
    second_list = webscraping_list(webpage, xpath_two)
    word_dict = {}
    altered_list =[]
    first_list = webscraping_list(webpage, xpath_one)
    second_list = webscraping_list(webpage, xpath_two)
    for item in second_list:
        item = item.replace('\xa0', '')
        print (item)
        altered_list.append(item)

    eng_words = webscraping_list(webpage, xpath_three)
    del eng_words[0] #probably a better way to do this. had text from the top of the table in the list so I just deleted the element at [0]

    print (first_list)
    print (altered_list)

    new_list = first_list
    for item in altered_list:
        if item != '':
            index = altered_list.index(item)
            print (index)
            new_list.insert( index, item)

    print(new_list)
    print (eng_words)

    index=0
    for item in first_list:
         print(first_list[index])
         print (eng_words[index])
         word_dict[first_list[index]] = {eng_words[index]}
         index+=1

    #print (word_dict)
    return word_dict

def webscraping_list(webpage, x_path):
    page = requests.get(webpage)
    tree = html.fromstring(page.content)

    list= tree.xpath(x_path)
    return list