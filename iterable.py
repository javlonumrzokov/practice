print("=======Iterable Objects =====")

# Iterable Objects: string, list, tuple, range, map, filter, dict
range_obj = range(3)
print("range_obj: ", range_obj)
for ele in range_obj:
    print(f"ele: {ele}")

for letter in "Python":
    print(f"letter: {letter}")


print("=======Dictionary =====")
# Dictionary: key value pair, unordered, mutable, JSON Object, key must be unique and immutable, value can be any type
person = {"name": "Jack", "age": 30, "single": "True"}
person_obj = dict(name="Jack", age=30, single="True")
print("person: ", person)
print("person_obj: ", person_obj)
# method: get()
# name = person.obj["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"name: {name}, hobby: {hobby}, balance: {balance}")
del person_obj["single"]
for key in person_obj:
    print(f"key: {key}, value: {person_obj.get(key)}")

    print("=======Error handling =====")

    car_dict = dict(name="Toyota", year=2026, electric=True)

    try:
        print("passed here")
        a = car_dict.speed
        result = car_dict["origin"]
        print("result:", result)

    # (KeyError`, AttributeError)`) or Exception as err: for all errors
    except KeyError as err:
        print("No origin state property found: ", err)
    except AttributeError as err:
        print("No speed property found: ", err)
    else:
        print("No error found")
    finally:
        print("This is finally block, always executed")
