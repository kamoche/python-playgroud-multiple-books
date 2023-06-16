def test(name, *others):
    print("First name %s" % name)
    print(others[0])
    print(others)
    for n in others:
        print(n)


test('jackson', 'githinji', 'kamoche', 'jkg')

print(test.__code__.co_argcount)
print(test.__code__.co_varnames)

from inspect import signature


def test1(nam, tribe='kukuyu'):
    print('%s %s ' % nam, tribe)


sig = signature(test1)
print(str(sig))
for n, param in sig.parameters.items():
    print(n, ":", param.default)

from collections import namedtuple

nt = namedtuple()
