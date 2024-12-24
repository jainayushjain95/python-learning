def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

map(square, my_nums)
print(my_nums)

my_nums = map(square, my_nums)
print(list(my_nums))


# for item in map(square, my_nums):
#     print(item)

# def check_even(num):
#     return num % 2 == 0
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# evens_list = list(filter(check_even, my_list))
# print(evens_list)


# value = lambda num: num**2
# print(value(5))
#
# my_nums = [1, 2, 3, 4, 5]
# print(list(map(lambda num: num**2, my_nums)))
# print(list(filter(lambda num: num % 3 == 0, my_nums)))