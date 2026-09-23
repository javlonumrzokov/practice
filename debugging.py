from PIL import Image
from turtle import Turtle, done

print("============Python Packages =========")


# Core packages https://docs.python.org/3/library

# t = Turtle()

# t.shape("turtle")
# t.speed(2)
# t.circle(140)

# done()

print("-----------------")

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with

with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE!")

# External Packages: https://pypi.org/

# Package managers: npm, yarn, pip, pipenv, composer, brew

'''
pip for windows and pip3 for MacOS
pip3 commands:
pip3 list, pip3 install pillow, pip3 uninstall pillow, pip3 show pillow, pip freeze > requirements.txt
'''

with Image.open("material/dolp.png") as img_obj:
    resized = img_obj.resize((200, 200))
    resized.show()
    resized.save("material/sample.png")


print("============ Debugging =========")


def get_sum(*args):  # DEFINE
    total = 0
    for a in args:
        total += a
        return total  # find the bug


test = 100
result = get_sum(1, 2, 3, 4, 5)  # CALL
print(f"result:", result)
