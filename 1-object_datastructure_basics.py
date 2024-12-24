name = "abcs"
name = name * 10

x = 'Hello World'
# print(x.upper())

my_list1 = [1, 2, 3]
my_list2 = [32, 1.12, 1, 2, 3]

my_list2 = my_list2 + my_list1

my_list2.sort()

my_dict = {"1": 2, "2": 3, "3": 4.2, 5.2: "132", '5.2': '123', "5.2": "13223"}
# print(my_dict['5.2'])

my_dict2 = {1: ['a', 'b', 'c']}
my_dict2.get(1)[1] = my_dict2.get(1)[1].upper()
# print(my_dict2.get(1)[1].upper())
# print(my_dict2.items())


tuple_sample = (1, 2, 3)
# print(type(tuple_sample))


print(set([1,1,2,3]))