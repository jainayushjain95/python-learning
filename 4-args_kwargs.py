# def myfunc(a, b):
#     return 0.05 * (a + b)
#
# def myfunc1(a, b):
#     return 0.05 * sum((a,b))

def myfunc2(*args):
    print(args)
    return 0.05 * sum(args)

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print(f'My fruit is: {kwargs["fruit"]}')
    else:
        print('Bakwaas')

def myfunc4(*args, **kwargs):
    print(f'I would like {args[0]} {kwargs["food"]}')

# print(myfunc2(10, 90, 1, 12, 413, 1231, 1231))
# myfunc3(fruit='apple')

myfunc4(30, fruit='apple', food='roti', drink='milk')