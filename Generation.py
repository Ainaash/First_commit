def doc_it(func):
    def new_func(*args, **kwargs):
        print('Running func:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_func
def add_ints(a, b):
    return a + b
add_ints(3,5)
cooler_add_ints = doc_it(add_ints) # создание декоратора вручную
cooler_add_ints(3, 5)
