def functiononly():
    print("hello world")

functiononly()


def add_number(a, b):
    """ Add two variable together
    
    Keyword arguments:
    a - first value
    b - second value
    """
    return a + b

result = add_number(5, 6)
print(result)
print(add_number("abc", "def"))

# parameter with default value make it optional when calling
def greet(name, message="Hello"):
    print(f"{message}, {name}")

# position argument
greet("Tom", "Have had your dinner?")
greet("Jerry")

# keyword argument
greet(message="I am hungry", name="Landy")

# Arbitrary Argument
def make_pizza(*toppings):
    print("making a pizza with the following toppings:")
    for topping in toppings:
        print(topping+" ", end="")

make_pizza("pepperoni", "mushrooms", "green peppers", "cheese")
print()

# Arbitrary Keyword Argument
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile

user_profile = build_profile("Michael", "Chen", location='Brisbane', role='Student', age=20)
print(user_profile)

# return data to caller
print(build_profile("Michael", "Chen", location='Brisbane', role='Student', age=20)["last_name"])


# print docstring for add_number function
print(add_number.__doc__)