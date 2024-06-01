# def isEven(number):
#     return number%2 == 0  

number = list(range(1, 13))
even_numbers = list(filter(lambda x: x % 2 == 0, number))

print(number)
print(even_numbers)

# same lambda function written in javascript
# let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
# let evenNumbers = numbers.filter(x => x % 2 === 0);

multiply = lambda a, b: a * b
print(multiply(4, 5))

# 
def myfunc(n):
    return lambda a: a*n

mydouble = myfunc(2)
print(mydouble(8))

tripler = myfunc(3)
print(tripler(8))
     
