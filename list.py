print("=======list =====")

# list: ordered, mutable, allows duplicates, can be used as key in dictionary
my_list = [1, 2, 3, 4, 5, "human", True]
print("my_list: ", my_list)

person = {"name": "Jack", "age": 30, "single": "True"}  # dictionary
people = ("ANDREW", "JOHN", "JANE")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"team: {team}")


print("============")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print(f"a: {a}, b: {b}, c: {c}, d: {d}")

print("======list methods======")

# append() insert() pop() remove() clear() index() count() sort() reverse() copy()

letters = ["a", "d", "b"]
letters.append("c")  # add behind the list
print(f"letters: {letters}")

letters.insert(0, "e")  # add front of the list
print(f"letters: {letters}")

size = len(letters)-1
letters.pop(size)  # remove last element of the list
print(f"letters: {letters}")

letters.pop(0)  # remove first element of the list
print(f"letters: {letters}")

letters.remove("b")  # remove specific element of the list
print(f"letters: {letters}")

animals = ["cat", "dog", "elephant", "tiger", "lion"]
del animals[2:4]  # delete specific element of the list [2:4)
print(f"animals: {animals}")

exist = "cat" in animals  # check if element exists in the list
print(f"exist: {exist}")
exist = animals.index("dog")  # get index of specific element in the list

print(f"exist: {exist}")

animals.clear()  # clear all elements of the list
print(f"animals: {animals}")

if "cat" in animals:
    print("cat exists in the list")
else:
    print("cat does not exist in the list")

animals2 = ["cat", "dog", "cat", "elephant", "tiger", "lion"]
print(f"animals2: {animals2}")
counter = animals2.count("cat")  # count specific element of the list

print(f"counter: {counter}")
# copy the list and gives a new reference to the copied list
animals3 = animals2.copy()
animals3.pop(0)  # remove first element of the list
print(f"animals3: {animals3}")
print(f"animals2: {animals2}")

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # sort the list in ascending order
print(f"numbers: {numbers}")

# numbers.sort(reverse=True)  # sort the list in descending order
# print(f"numbers: {numbers}")

numbers.reverse()  # reverse the list
print(f"numbers: {numbers}")

# sort the list in ascending order and gives a new reference to the sorted list
new_numbers = sorted(numbers)  # immutable
print(f"new_numbers: {new_numbers}")
print(f"numbers: {numbers}")

print("=======lambda function =====")  # small anonymous function
def calculate(x, y): return x + y


result = calculate(5, 10)
print(f"result: {result}")

people = [("John", 25),
          ("Jane", 30),
          ("Alice", 20),
          ("Bob", 35)
          ]
people.sort()
print(f"people: {people}")
people.sort(key=lambda x: x[0])  # sort by name
print(f"people: {people}")
people.sort(key=lambda person: person[1])  # sort by age
print(f"people: {people}")
