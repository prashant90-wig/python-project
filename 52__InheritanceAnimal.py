class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def main():
    dog = Dog("Husky")
    cat = Cat("Kitty")
    
    print(dog.speak())
    print(cat.speak())

if __name__ == "__main__":
    main()