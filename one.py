def func1():
    print("one.py->func1()")

print("Top Level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported")