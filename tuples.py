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
