class ManageFile:

    def __init__(self, name, option='r'):
        self.name = name
        self.option = option

    def __enter__(self):
        self.file = open(self.name, self.option)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


from contextlib import contextmanager


@contextmanager
def manage_file(name, option='r'):
    try:
        f = open(name, option)
        yield f
    finally:
        f.close()


with ManageFile('kamoche.txt', 'w') as f:
    f.write('Custom context manager')

with manage_file('kamoche.txt', 'w') as f:
    f.write('Custom context manager')
