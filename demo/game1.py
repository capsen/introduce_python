import pgzrun
import random
x = 0
y = 0

WIDTH = 800
HEIGHT = 600

#Add your code below
runner = Actor("p3_stand")
runner.pos = (60, 400)
runner.images= ['p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05', 'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09','p3_walk10', 'p3_walk11']
runner.imageindex = 0
runner.velocity_y = 0
runner.is_jump = False
gravity = 1
score = 0
game_over = False

obstacles=[]
obstacles_timeout=50

def draw():
    screen.draw.filled_rect(Rect(0,0,800,400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    if game_over:
        screen.draw.text("Game Over", (300, 300), color="red", fontname="bauhs93", fontsize=30)
    else:
        screen.draw.text(str(score), (50, 30), color="red", fontname="bauhs93", fontsize=30)
        runner.draw()
        for obstacle in obstacles:
            obstacle.draw()

def update():
    # any global variable need to be updated need specify global
    global obstacles_timeout, score, game_over

    if game_over:
        return
    # p3.left += 2
    # if(p3.left > 800):
    #     p3.right = 0

    if(runner.imageindex > len(runner.images)-1):
        runner.imageindex=0
    runner.image=runner.images[runner.imageindex]
    runner.imageindex += 1

    if keyboard.space:
        if runner.is_jump == False:
            runner.velocity_y = -20
            sounds.jump.play()
            runner.is_jump = True

    runner.y += runner.velocity_y
    runner.velocity_y += gravity

    #back to ground
    if runner.y > 400:
        runner.velocity_y = 0
        runner.y = 400
        runner.is_jump = False

    obstacles_timeout -=1
    if obstacles_timeout < 0:
        obstacle = Actor('cactus')
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = random.randint(25, 60)
    
    for obstacle in obstacles:
        obstacle.left -= 8
        if obstacle.right < 0:
            score += 1
            sounds.point.play()
            obstacles.remove(obstacle)
    
    if runner.collidelist(obstacles) != -1:
        game_over = True
        sounds.die.play()

pgzrun.go() # Must be last line