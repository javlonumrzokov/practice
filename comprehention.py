print("=======Comprehentions =====")

# Comprehention acts like spread operator in JS, it spreads the values of an iterable into a new list, set, or dictionary.

'''
comprehention general syntsax:
a) *iterable
b) <expression> for <item> in <iterable>
c) <expression> for <item> in <iterable> if <condition>
'''

# List Comprehension

numbers = [1, 2, 3, 4, 5]
list_numbers = [*numbers]  # spreads the values of numbers into a new list
print(f"list_numbers: {list_numbers}")
print(numbers is list_numbers)  # False, because they are different objects
print(id(numbers), id(list_numbers))  # different memory addresses

people = [("Alice", 25), ("Bob", 30), ("Charlie", 35), ("David", 40)]

# Create a new list of names using list comprehension
names = [person[0] for person in people]
age_list = [person[1] for person in people]
print(f"names: {names}")
print(f"age_list: {age_list}")


cars = [
    ("Toyota", 78),
    ("Honda", 23),
    ("Ford", 109),
    ("Chevrolet", 15)
]

list_cars = [car[0] for car in cars if car[1] > 30]

print(f"list_cars: {list_cars}")

# Set and dicttionary Comprehension

numbs = [1, 2, 4,  3, 4, 2, 2, 5]
set_numbs = {*numbs}  # a version
print("set_numbs:", set_numbs)


dict_people = {person[0]: person[1] for person in people}  # b version
print(f"dict_people: {dict_people}")

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 25}  # version c
print(f"dict_people2: {dict_people2}")
