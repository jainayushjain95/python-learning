# # mylist = [1, 2, 3, 4]
# # print(mylist)
# # mylist.pop()
# # print(mylist)
# #
# # help(mylist.pop())
# def say_hello():
#     for x in range(10):
#         print("Hello World!")
#
# def say_hello2(name = 'Default Name'):
#     print(f"Hello {name}")
#
# say_hello2('Ayush')
# say_hello2()
#
# def add_num(num1, num2):
#     num1 = 0
#     return num1 + num2
#
# num1 = 10
# num2 = 20
#
# result = add_num(num1, num2)
# print(num1)


# def check_if_even_exists(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             return True
#         else:
#             pass
#     return False
#
# def get_all_evens(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers
#
# mylist = [1,2,9,132,1,1,2,3,4,4,5,5,6]
# print(get_all_evens(mylist))


# work_hours = [('A', 800), ('B', 1200), ('C', 500), ('D', 400), ('E', 510)]
#
# def get_employee_of_the_year(work_hours_list):
#     max_hours = -1
#     employee_name = ''
#     for name, hours in work_hours_list:
#         if hours > max_hours:
#             max_hours = hours
#             employee_name = name
#     return max_hours, employee_name
#
# print(get_employee_of_the_year(work_hours))

from random import shuffle, randint

def shuffle_my_list(my_list):
    shuffle(my_list)
    return my_list

def is_valid_guess(guess_value):
    return guess_value == '0' or guess_value == '1' or guess_value == '2'

def player_guess():
    guess_value = ''
    while not is_valid_guess(guess_value):
        guess_value = input('Guess a number [0, 2]')
    return int(guess_value)

def check_guess(my_list, guess_value):
    if my_list[guess_value] == 'O':
        print('Correct!')
    else:
        print('Wrong!')
        print(my_list)

mylist = shuffle_my_list([' ', 'O', ' '])

for num in range(1, 5):
    mylist = shuffle_my_list(mylist)
    guess = player_guess()
    check_guess(mylist, guess)