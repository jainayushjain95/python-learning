# def func():
#     return 1
#
# def hello():
#     return 'Hello!'
#
# greet = hello
# print(greet())
#
# del hello
#
# print(greet())

# def hello(name='Ayush'):
#     print(f'Hello {name}!')
#     def greet():
#         return '\t This is a greeting! inside hello'
#     def welcome():
#         return '\t This is a welcome inside hello'
#     print(greet())
#     print(welcome())
#     print('End of hello')
#
# hello()

# def hello(name='Ayush'):
#     print(f'Hello {name}!')
#     def greet():
#         return '\t This is a greeting! inside hello'
#     def welcome():
#         return '\t This is a welcome inside hello'
#     print('Returning a function')
#     if(name == 'Ayush'):
#         return greet
#     else:
#         return welcome
#
# my_new_func = hello('asd')
# print(my_new_func())

# def hello():
#     return 'Hi Ayush'
#
# def other(some_defined_function):
#     print('Other code runs here')
#     print(some_defined_function())
#
# other(hello)

def new_decorator(original_function):
   def wrap_func():
       print('Some extra code before the original function')
       original_function()
       print('Some extra code after the original function')
   return wrap_func

# def func_needs_decorator():
#     print('I want to be decorated')

# func_needs_decorator()
# decorated_function = new_decorator(func_needs_decorator)
# decorated_function()


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
func_needs_decorator()