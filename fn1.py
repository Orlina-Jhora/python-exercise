name=input("Input your name:")
def greet(name, greeting="Hello"):
    return (f"{greeting}, {name}!")

print(greet(name, greeting="Hello"))               
print(greet(name, "Good morning"))  