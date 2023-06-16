# Old style
errno = 50159747054
name = 'Bob'

print(' Hello %s' % name)
print('%x ' % errno)

print('Hey %s, there is a 0x%x error!' % (name, errno))

print('Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno})


#New style python 2.7 and 3

print('Hello, {}'.format(name))
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))


#Python 3.6

print(f'Hello, {name}!')

a = 5
b = 10

print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')


print(f"Hey {name}, there's a {errno:#x} error!")

from string import Template

t = Template('Hey, $name!')
print(t.substitute(name=name))


templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))