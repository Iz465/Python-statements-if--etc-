class Dog:
    # Class attribute
    attr = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation

Rodger = Dog("Roger")
Tommy = Dog("Tommy")


# Accessing class attribute
print("Rodger is a {}".format(Rodger.__class__.attr))
print("Tommy is also a {}".format(Tommy.__class__.attr))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))




# Example Two 
print("\nExample Two")

# Accessing class methods
Rodger.speak()
Tommy.speak()
