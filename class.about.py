class Person():
    # state
    message = "state property of class Person"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    @classmethod
    def explain(cls):
        print("static method property executed")
        return f"This is a class method. The message is: {cls.message}"


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# ordinary state
name = person1.name
print(f"name: {name}")

# ordinary method
person1.greet()
person2.greet()
person3.greet()

Person.explain()
