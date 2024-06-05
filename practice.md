# Introduce_python

## Practice Workshop 2
1.  Convert Inch and cm

* Create a python file **InchCmConverter.py**
* 1 inch = 2.54 cm
* In your code you need use print() input() str() and float()

### Example Output
```bash
Welcome to Inch CM Converter
Please enter the value of Inch: 34
34 inch = 86.36 cm
```

2.  Calculate average
* Create a python file average.py allow user to find average number from a group of numbers
* You need let people enter the number again if user didn't enter a number
* To achieve this you need use a list, if else condition, while and for loops, isdecimal() print() input() str() float() methods

### Example Output
```bash
Please enter how many number you going to enter: d
The text you entered is not a number!

Please enter how many number you going to enter: 3
please enter a number: 23
please enter a number: 23
please enter a number: 18.9

The average number is 24.96666666667
```

3.  Calculate max, min, total, average
* Create a python file exercise3.py allow user to find max and min number and the index of that number, total and average number from a group of numbers
* You need let people enter the number again if user didn't enter a number
* To achieve this you need use a list, if else condition, while and for loops, isdecimal() print() input() str() float() methods. Please make sure all the number people entered is stored in a list.

### Example Output
```bash
Please enter how many number you going to enter: d
The text you entered is not a number!

Please enter how many number you going to enter: 3
please enter a number: 23
please enter a number: 23
please enter a number: 18.9

The max number is 23 and position at 0
The min number is 18.9 and position at 2
The total is 64.9
The average number is 24.96666666667
```

## Practice Workshop 4
1. Create a python file **powerball.py** to generate a number of random Powerball numbers. The output should be like below

   - You need create a function name picknumbers which will take two parameter **poolsize** and **ballnum**

   - To generate one set of power ball numbers you can call method print(picknumbers(35, 7), picknumbers(20, 1))

   - Tips: Please use list(range(start,end)) to generate a list of the numbers and then use random.shuffle() method to shuffle the numbers each time before pick a number

   - To achieve this you need use a list, while loops, print() input() list.append() list.pop() methods


## Practice Workshop 5
1. Create a python file **combine.py** to let people enter the filename in the data folder. (Please exclude the "-A.txt" in the file name). Then it will read <filename-A.txt> and <filename-B.txt> file, read each line from each file and combine them line by line, odd line be A.txt file and even line be B.txt file. Save the combined text and save to <filename-out.txt> file. Also print out the content to see what's the picture generated.

## Practice Workshop 6
1. Define a Book Class

```
Attributes: title, author, isbn, price, stock
Methods: display_info(), add_stock(), sell_book()
```

2. Define a Specialized Book Class
```
Create a subclass of Book called EBook with an additional attribute for file format (file_format).
```

3. Create an Inventory Class
```
Attributes: books (a list to store Book objects)
Methods: add_book(), remove_book(), find_book(), display_inventory()
```

4. Main Program
```
Create an instance of Inventory
Add a few books to the inventory
Display the inventory
Simulate selling a book and updating the stock
```

## Practice Workshop 7
### Make a walking Alien
1. Create a python file game1.py then do following steps
add basic code for pygame zero to create a window with 800 width and 600 height
```python
import pgzrun

WIDTH = 800
HEIGHT = 600

#Add your code below

pgzrun.go() # Must be last line
```

2. Add a new line after #Add your code below comment, then create a draw() function to set the background with two rectangle for sky and grass
```python
def draw():
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
```

3. Create an actor and assign to variable p1 and set position to x=400 and y=400 position the code after HEIGHT = 600 line 4
```python
p3 = Actor("p3_stand")
p3.pos = (400, 400)
```
4. Now create an update function after draw function to update actor position. remember every time when actor moved out of the screen move it back to left of the screen
```python p3.left += 2
    if(p3.imageindex > len(p3.images)-1):
        p3.imageindex=0
```

5. Last:(Challenge) you need add another two property to the actor, one is images to store a list of the image, and imageindex to store current index of the image. Then add your own code to update the image property to loop through the images everytime when update() been called. Make sure the index won't exceed the last index of the images array. You have to work our your own solution.
```python
p3.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
p3.imageindex = 0
```

### Make a Runner Game
1. Continue with the game1.py, comment out the code for p3 (alien) to stop it move from left to right, and position p3 to (100, 400) for the start position

2. Make the p3 able to dump when click space button on the keyboard. To achieve this you need set initial velocity_y and gravity variable for p3
```python
p3.velocity_y = 0
p3.gravity = 2
```

3. Then, add following code inside update() method to allow handle space key event and set the velocity_y to -15 to give initial velocity.
```python
    # make p3 jump if space pressed
    if keyboard.space:
        p3.velocity_y = -15
    p3.y += p3.velocity_y
```

4. You will find the Alien will be able jump after you press space key but never drop back to ground. That is because you didn't apply the gravity to the velocity. To achieve this you can use following code.
```python
    p3.velocity_y+=p3.gravity

    if p3.y>400:
        p3.velocity=0
        p3.y=400
```

5. Now you need add some obstacles, to do that you need maintain two variables, one is a list obstacles to store all obstacle object, another is obstacles_timeout to control the time difference between each obstacle
```python
obstacles=[]
obstacles_timeout=0
```

6. We also need move the obstacles from right to left, please add following code inside update function
```python
    global obstacles_timeout
    obstacles_timeout +=1
    if obstacles_timeout > 50:
        obstacle = Actor('cactus')
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = 0
```

7.You will find out the obstacles are not appearing on the screen when you run the code, that's because you need draw those obsticles in draw() function
```python
    for obstacle in obstacles:
        obstacle.draw()
```

8. Last thing is you need to remove the obstacles when they move out of the screen, otherwise you will run out memory after a period of time. Please add following code at the end of update function
```python
    for obstacle in obstacles:
        obstacle.left -= 8
        if obstacle.right < 0:
            obstacles.remove(obstacle)
```
![game video](assets/game1.mp4)

