count = ""
while (not count.isdecimal()):
    count = input("Please enter how many number you going to enter: ")

sum = 0
for i in range(int(count)):
    number = input("please enter a number:")
    sum = sum + float(number)

print("The average number is", sum/int(count))
