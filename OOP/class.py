class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age

dog1 = dog("Buddy", 3)
dog2 = dog("Max", 5)
print(dog1.bark())  # Output: Buddy says woof!
print(f"{dog1.name} is {dog1.get_age()} years old.")  # Output: Buddy is 3 years old.
print(dog2.bark())  # Output: Max says woof!
print(f"{dog2.name} is {dog2.get_age()} years old.")  # Output: Max is 5 years old.