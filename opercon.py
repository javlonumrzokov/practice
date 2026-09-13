print("=======Operations =====")

a = 5
b = 10
print('a**2:', a**2)
print('b**3:', b**2)

# only in python string can be multiplied by an integer to repeat the string
print("j"*5)

c = dict(name="Alice", age=30)
d = dict(name="Alice", age=30)
e = c

print("c == d:", c == d)  # True, because the contents are the same

# Different memory addresses for c and d, same for e
print(id(c), id(d), id(e))
print("c is d:", c is d)  # False, because they are different objects
print("c is e:", c is e)  # True, because e references the same

print("=======Conditions=====")


x = 5

if x > 50:  # checks truthy or falsy value of the expression
    print('x is greater than 50')
elif x > 10:
    print('x is greater than 10')
else:
    print('other case')

    # Ternary operator: value_if_true if condition else value_if_false

age = 18

person = "adult" if age >= 18 else "minor"
print(f"person: {person}")

isStudent = True
isParent = False
isAdmin = False
isLoggedIn = True

if not isStudent:
    print("User is a student")
elif isParent:
    print("User is a parent")
elif isAdmin and isLoggedIn:
    print("User is an admin and logged in")
else:
    print("User is not a student, parent, or admin")
