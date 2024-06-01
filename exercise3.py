count = ""
numbers=[]
while (not count.isdecimal()):
    count = input("Please enter how many number you going to enter: ")

for i in range(int(count)):
    number = input("please enter a number:")
    numbers.append(float(number))

max_number=max(numbers)
min_number=min(numbers)
total=sum(numbers)

print(f'The max number is {max_number} and position at {numbers.index(max_number)}')
print(f'The min number is {min_number} and position at {numbers.index(min_number)}')
print(f"The total is {sum(numbers)}")
print(f'The average number is {sum(numbers)/len(numbers)}')


# print("The max number is", max(numbers), "and position at", numbers.index(max(numbers)))
# print("The min number is",min(numbers), "and position at", numbers.index(min(numbers)))
# print("The total is", sum(numbers))
# print("The average number is", sum(numbers)/len(numbers))



