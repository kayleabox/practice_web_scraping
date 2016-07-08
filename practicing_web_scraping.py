from lxml import html
import requests

page = requests.get('http://masterrussian.com/vocabulary/common_verbs.htm')
tree = html.fromstring(page.content)

word_dict = {}
rus_words_add =[]
rus_words = tree.xpath('//*[@ class = "word"]/a/text()')
rus_words_two = tree.xpath('//*[@ class = "word"]/text()')
for item in rus_words_two:
    item = item.replace('\xa0', '')
    print (item)
    rus_words_add.append(item)


"""rus_words.add(tree.xpath('//*[@ class = "word"]/text()'))"""
"""rus_words = tree.xpath('//tr/td [@ class = "word"]/a/text()')"""
eng_words = tree.xpath('//tr/td [3]/text()')
del eng_words[0] #probably a better way to do this. had text from the top of the table in the list so I just deleted the element at [0]


print (rus_words)
print (rus_words_add)

new_rus_words = rus_words
for item in rus_words_add:
    if item != '':
        index = rus_words_add.index(item)
        print (index)
        new_rus_words.insert( index, item)

print(new_rus_words)
print (eng_words)

index=0
for item in rus_words:
     print(rus_words[index])
     print (eng_words[index])
     word_dict[rus_words[index]] = {eng_words[index]}
     index+=1

print (word_dict)