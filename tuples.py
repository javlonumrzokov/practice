# literal
nums = [1, 2, 3, 4, 5]  # list
car_dict = {"name": "Toyota", "year": 2026, "electric": True}  # dictionary


print(nums)
# constructor
letters = list("Python")  # list
person_dict = dict(name="Jack", age=30, single="True")  # dictionary
print(letters)

# tuple: immutable, ordered, allows duplicates, can be used as key in dictionary
print("=======Tuple =====")
my_tuple = (1, 2, 3, 4, 5, "human", True)
print("my_tuple: ", my_tuple)

avoiding_type = "hi", "hello", "hey"  # tuple

print("=======Unpacking arguments(destructuring) =====")

# yoki ("Group A", "Group B", "Group C", "Group D")
groups = ["Group A", "Group B", "Group C", "Group D"]
(group1, group2, *group3) = groups
print(f"group1: {group1}, group2: {group2}, group3: {group3}")


def calculate_sum(*args):
    total = 1
    for num in args:
        total += num
    print(f"args: {args}, total: {total}")
    return total


# CALL
calculate_sum(1, 2, 3, 4, 5)
print("------------------")


def introduce(**kwargs):
    print(
        f"Hello, my name is {kwargs['name']}. I am {kwargs['age']} years old ")


# CALL
introduce(name="Alice", age=30, city="New York")
print("------------------")


def greetings(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")


# CALL
greetings("Hello", "Hi", name="Alice", age=30)
print("------------------")

print("=======zip =====")

tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")
zipped = zip(tuple1, tuple2)
print("zipped: ", zipped)

result = list(zipped)
print("result: ", result)


print("=======enumerate, map and filter =====")

# enumerate: returns an enumerate object, which is an iterator that produces pairs of index and value for each item in the input iterable.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"index: {index}, fruit: {fruit}")

print("------------------")

# similar in dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
# returns a view object that displays a list of a dictionary's key-value tuple pairs
result = person.items()
print("result: ", result)
for (key, value) in result:
    print(f"key: {key}, value: {value}")

print("------------------")

# yoki togridan togri quyidagicha
for index, (key, value) in enumerate(person.items()):
    print(f"index: {index}, key: {key}, value: {value}")


print("------------------")
# map: applies a function to each item in an iterable and returns an iterator that yields the results.
cars = [
    ("Toyota", 78),
    ("Honda", 23),
    ("Ford", 109),
    ("Chevrolet", 15)
]
new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars: ", new_cars)

result1 = map(lambda car: car[0], cars)
print(f"result1:  {result1} type: {type(result1)}")
new_cars2 = list(result1)
print("new_cars2: ", list(new_cars2))

print("------------------")

# filter: constructs an iterator from elements of an iterable for which a function returns true.

result_filter = filter(lambda car: car[1] > 50, cars)
print(f"result_filter:  {list(result_filter)} type: {type(result_filter)}")
