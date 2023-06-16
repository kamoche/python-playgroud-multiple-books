def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def bare_bones():
    while True:
        value = (yield)
        print(value)


cor = bare_bones()
cor.send("Using a decorator!")
