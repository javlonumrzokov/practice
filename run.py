# Dunder __builtins__, __init__
message = "In Python Everything is object!"
print(message)
result = type(message)
print("result", result)

''' In python there are built in tools:
Types: int float str list dict
Funtctions: print() len() inpput() type() str() int()
Constants: TRUE FALSE NONE
'''
print(dir(__builtins__))
