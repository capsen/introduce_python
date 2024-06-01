def add_numbers(a, b):
    print(a,b)
    print(a,b)
    print(a,b)
    print(a,b)
    print(a,b)
    print(a,b)
    return int(a) + int(b)

def multiply_numbers(a, b):
    return a * b

def calculate(a, b):
    sum_result = add_numbers(a, b)
    product_result = multiply_numbers(a, b)
    print("Sum:", sum_result)
    print("Product:", product_result)

# Calling the function with incorrect values to demonstrate debugging
calculate('3', 5)