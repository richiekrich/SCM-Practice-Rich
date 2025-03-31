# This feature greets the stored person's name
def greet(name):
    print(f"Hello, {name}!")

def name_length(name):
    length = len(name)
    print(f"The name {name} has {length} characters.")

greet("Alice")
greet("Daniel")

name_length("Alice")
name_length("Daniel")
