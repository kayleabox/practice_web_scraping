import make_dict_quizlet_fun as make_dict


webpage = 'https://quizlet.com/8557367/most-common-russian-verbs-flash-cards/'
xpath_one = '//*[@ class="TermText qWord lang-ru"]/text()'
xpath_two = '//*[@ class="TermText qDef lang-en"]/text()'

word_dict = make_dict.webscraping_dict(webpage, xpath_one, xpath_two)

print('word dict = ', word_dict)