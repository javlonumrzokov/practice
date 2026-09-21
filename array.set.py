from array import array
print("=======array =====")


numbers = array("i", [1, 4, 6, 23, 20, 128])
print(f"numbers: {numbers}")
del numbers[0:2]
print(f"numbers2: {numbers}")

print("=======set =====")

new_num = array("i", [1, 4, 6, 4, 23, 20, 4, 128])
set_numbers = set(new_num)
print(f"set_numbers: {set_numbers}")


print("=======specific operators withset =====")

a = {20, 10, 50}
b = {40, 10}

result1 = a | b  # a.union(b)  # union of two set``
print(f"result1: {result1}")
result2 = a & b  # a.intersection(b)  # intersection of two set
print(f"result2: {result2}")
result3 = a - b  # a.difference(b)  # difference of two set
print(f"result3: {result3}")
result4 = a ^ b  # a.symmetric_difference(b)  # symmetric difference of two set
print(f"result4: {result4}")
