# from collections import Counter
# my_list = [1, 1, 1, 1, 2, 2, 4, 5, 6, 6, 6, 3, 3, 9, 10]
#
# print(Counter(my_list).keys())
import os
from collections import defaultdict
# d = {'a': 10}
# print(d['qw'])

# d = defaultdict(lambda : 0)
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# print(d['qw'])

# f = open('practice.txt', 'w')
# f.write('Test string 1')
#
# import os
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir("/Users/ayushjain/Desktop/projects"))

import shutil
# shutil.move('practice.txt', os.getcwd() + '/MyMainPackage/' + 'practice.txt')
# shutil.copy(os.getcwd() + '/MyMainPackage/' + 'practice.txt', 'practice1.txt')
# shutil.copy(os.getcwd() + '/MyMainPackage/' + 'practice.txt', 'practice2.txt')
# shutil.copy(os.getcwd() + '/MyMainPackage/' + 'practice.txt', 'practice3.txt')

# import send2trash
# send2trash.send2trash('practice1.txt')

# for folder, sub_folders, files in os.walk('.'):
#     print(f'\nfolder: {folder}')
#     for sub_folder in sub_folders:
#         print(f'\tsub_folder: {sub_folder}')
#         for file in files:
#             print(f'\t\tfile: {file}')

# import datetime
# mytime = datetime.time(2, 20)
# print(mytime.second)
#
# today = datetime.date.today()
# print(today)
#
# import math
# print(help(math))

import pdb

x = [1,2,3]
y = 2
z = 3

result1 = y + z

pdb.set_trace()

result2 = x + y
