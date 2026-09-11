print("=======number =====")
# in Java, variable is named staorage location
# in Python variable is named reference

count = 100
count_type = type(count)

print(f"count: {count}  and type of it: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("=======string =====")
# Methods: upper() lower() title() find() replace()

course = "AI python Fullstack"
result = type(course)
print(f"the result(1) : {result}")

result = course.upper()
print(f"the result(2) : {result}")

result = course.replace("Fullstack", "Matterclass")
print(f"the result(3) : {result}")

print("=======boolean =====")
# functions type() input() int() str() bool()
y = input("Enter input for y: ")
print("y:", y)

result = y.isnumeric()
print(f"input value is numeric: {result}")

test_truthy = "MIT"
print("test truthy: ", bool(test_truthy))
