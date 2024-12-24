# def create_cubes(n):
#     result = []
#     for i in range(n):
#         result.append(i**3)
#     return result
#
# for x in create_cubes(10):
#     print(x)

def create_cubes(n):
    for i in range(n):
        yield i**3

for x in create_cubes(10):
    print(x)