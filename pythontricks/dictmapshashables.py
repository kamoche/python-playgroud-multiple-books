from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType

numbers = OrderedDict(one=1, two=2)

dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:

dd['dogs'].append('Rufus')

dict1 = {'one': 1, 'two': 2}

dict2 = {'three': 3, 'four': 4}

chain = ChainMap(dict1, dict2)


read_only = MappingProxyType(dict1)