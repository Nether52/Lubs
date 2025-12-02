# main.py

from decorator import count_same_args

@count_same_args
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2, 3))
print(add(5, 1))
print(add(2, 3))
print(add(5, 1))
