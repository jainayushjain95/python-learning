# x = 25
# def printer():
#     x = 50
#     return x
#
# print(x)
# print(printer())


# #Global
# name = 'THIS IS A GLOBAL STRING'
# def greet():
#     #Enclosing
#     name = 'Sammy'
#     def hello():
#         #Local
#         name = 'Ayush'
#         print(f'Hello there: {name}')
#     print(f'Hello there: {name}')
#     hello()
# print(f'Hello there: {name}')

# greet()


#Global
name = 'THIS IS A GLOBAL STRING'
def greet():
    #Enclosing
    global name
    print(f'Hello there2: {name}')
    name = 'Name changed'
    print(f'Hello there3: {name}')

greet()
print(f'Hello there1: {name}')