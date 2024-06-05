import pgzrun
x = 0
y = 0

WIDTH = 800
HEIGHT = 600

#Add your code below
p3 = Actor("p3_stand")
p3.pos = (60, 400)
p3.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
p3.imageindex = 0
p3.velocity_y = 0
gravity = 1

obstacles=[]
obstacles_timeout=0

def draw():
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    p3.draw()

    for obstacle in obstacles:
        obstacle.draw()

def update():
    # p3.left += 2
    # if(p3.left > 800):
    #     p3.right = 0

    if(p3.imageindex > len(p3.images)-1):
        p3.imageindex=0
    p3.image=p3.images[p3.imageindex]
    p3.imageindex += 1

    if keyboard.space:
        p3.velocity_y = -15

    p3.y += p3.velocity_y
    p3.velocity_y += gravity

    if p3.y > 400:
        p3.velocity_y = 0
        p3.y = 400

    global obstacles_timeout
    obstacles_timeout +=1
    if obstacles_timeout > 50:
        obstacle = Actor('cactus')
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = 0
    
    for obstacle in obstacles:
        obstacle.left -= 8
        if obstacle.right < 0:
            obstacles.remove(obstacle)

pgzrun.go() # Must be last line