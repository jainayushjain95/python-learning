import time

def func1(n):
    print("Hi\n")
    return [str(num) for num in range(n)]


def func2(n):
    return list(map(str, range(n)))


start = time.time()
result1 = func1(10)
end1 = time.time()

print(end1 - start)

result2 = func2(10)
end2 = time.time()
print(end2 - end1)

import timeit
stmt = '''
func1(100)
'''

setup = '''
def func1(n):
    print("Bi") 
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup=setup,number=1))
