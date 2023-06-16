import json
import pprint

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

# >>> json.dumps(mapping, indent=4, sort_keys=True)
# {
# "a": 23,
# "b": 42,
# "c": 12648430
# }

# >>> json.dumps({all: 'yup'})
# TypeError: "keys must be a string"


# >>> mapping['d'] = {1, 2, 3}
# >>> json.dumps(mapping)
# TypeError: "set([1, 2, 3]) is not JSON serializable"


# >>> pprint.pprint(mapping)
# {'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}