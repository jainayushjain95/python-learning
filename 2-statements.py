# a = 6;
# if a > 10:
#     print("10")
# elif a > 5:
#     print("5")
# else:
#     print("1")

# mylist = [1,2,3,4,5,6,7,8,9,10]
# for num in mylist:
#     if num % 2 == 0:
#         print(num)

# name = 'Hello World'
# for c in name:
#     print(c)
#
#
# mytuplist = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# for (a, b) in mytuplist:
#     print(str(a) + ', ' + str(b))
#
# for a, b in mytuplist:
#     print(str(a) + ', ' + str(b))

# dict = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
# for item in dict:
#     print(item + str(dict[item]))

# x = 0
# while x < 5:
#     print(x)
#     x = x + 1
# else:
#     print("Finished")

# x = 50
# while x < 5:
#     print(x)
#     x = x + 1
# else:
#     print("Finished")

# x = [1, 2, 3]
# for item in x:
#     #A comment
#     pass

# for num in range(3,10,2):
#     print(num)

# index = 0
# name = "abcde"
# for c in name:
#     print("At index {}, character is: {}".format(index, c))
#     index += 1

# for item in enumerate(name):
#     print(item)
#
# for index, letter in enumerate(name):
#     print(index, letter)

#
# mylist1 = [1, 2, 3]
# mylist2 = [4, 5]

# for item in zip(mylist1, mylist2):
#     print(item)

# for i1, i2 in zip(mylist1, mylist2):
#     print(i1, i2)
#
# print('x' in [1, 2, 'x', 3])

# mylist1 = [1, 2, 3]
# print(min(mylist1))

# from random import shuffle
# shuffle(mylist1)
# print(mylist1)

# from random import randint
# print(randint(1, 3))


# result = input('Hey Enter a no')
# print(result)
# print(type(result))

name = 'Hello'
# mylist = []
# for letter in name:
#     mylist.append(letter)
# print(mylist)

# mylist = [letter for letter in name]
# print(mylist)

# mylist = [num for num in range(1, 10)]
# print(mylist)

# mylist = [num*3 for num in range(1, 10)]
# print(mylist)

mylist = [num for num in range(1, 10) if num % 2 == 0]
print(mylist)