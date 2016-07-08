import make_dict_webscraping as make_dict

webpage = 'http://masterrussian.com/vocabulary/common_verbs.htm'
xpath_one = '//*[@ class = "word"]/a/text()'
xpath_two = '//*[@ class = "word"]/text()'
xpath_three = '//tr/td [3]/text()'

word_dict = make_dict.webscraping_dict(webpage, xpath_one, xpath_two, xpath_three)

print('word dict = ', word_dict)
