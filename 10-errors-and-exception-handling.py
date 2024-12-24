# def add(n1, n2):
#     return n1 + n2
#
# number1 = 10
# number2 = input('Please provide a no')
# try:
#     result = add(number1, number2)
# except:
#     print('Something went wrong')
# else:
#     print(result)
#
# print("Done")

# try:
#     f = open('testfile', 'r')
#     f.write("Write a test line")
# except TypeError as type_error:
#     print(f"There was an TypeError: {type_error}")
# except OSError as os_error:
#     print(f"There was an OSError: {os_error}")
# except:
#     print(f"There was an Unexpected error: {sys.exc_info()[0]}")
# finally:
#     print("Finally!")

def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number"))
        except:
            print("Invalid input")
            continue
        else:
            print(f"Valid input: {result}")
            break
        finally:
            print("Finally!")

ask_for_int()