
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['kamoche']  = 'scala'
favorite_languages['jackson'] = 'java'
favorite_languages['githinji'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + " favorite language is " + language.upper())