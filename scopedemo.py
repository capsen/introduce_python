#global scope
x = 600
# local scope
def myfunc():
    global x
    x = 300
    def myinnerfunc():
        x=500
        x=3*x
        print(x)
    myinnerfunc()
    print(x)

myfunc()
print(x)