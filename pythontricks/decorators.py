import functools


def uppercase(func):
    @functools.wraps(func)
    def modify_result():
        unmodified_result = func()
        modified_result = unmodified_result.upper()
        return modified_result

    return modify_result


@uppercase
def greet():
    return 'hello'


print(greet())


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'

    return wrapper


@strong
@emphasis
def greet():
    return 'hello'


print(greet())

decorated_greet = strong(emphasis(greet))
print(decorated_greet)
print(strong(emphasis(greet)))


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() ', f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() ', f'with args {args}, kwargs {kwargs} ', f'returned {original_result!r}')
        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('kamoche', 'cool')
