# Program to demonstrate identity operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)         # False (different objects with same value)
print(a is c)         # True (same object)
print(a is not b)     # True (not the same object)
