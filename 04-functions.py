def add(a, b):
    return a + b


print(add(2, 3))


# Arbitrary Arguments *args
def add_all(*args):
    print(args)
    return sum(args)


print(add_all(1, 2, 3))


# Keyword Arguments **kwargs
def show_info(**kwargs):
    print(kwargs)

show_info(name="Joshua", age=26)