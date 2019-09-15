import pygame as pg
import random
import math

WIN_HEIGHT = 500
WIN_WIDTH = 500
isRun = True

win = pg.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
pg.display.set_caption("Carrom?")
group = pg.sprite.Group()

class Coin(pg.sprite.Sprite):
    def __init__(self, coin_x, coin_y, clr=(255,0,0)):
        super().__init__()
        self.color = clr
        self.center = (coin_x, coin_y)
        self.radius = 12
        self.speedX = random.randint(5, 8)
        self.speedY = 0#random.randint(5, 8)
        group.add(self)
        self.drawMe(self.center)


    def drawMe(self, center):

        self.rect = pg.Rect(pg.draw.circle(win, self.color, center, 12))
        self.center = center


    def updateX(self):
        x = self.center[0]
        y = self.center[1]
        if self.speedX > 0:
            if x + 12 + self.speedX >= 500:
                self.speedX = -self.speedX
        else:
            if x - 12 - self.speedX <= 0:
                # print("1")
                self.speedX = -self.speedX
        if self.speedY > 0:

            if y + 12 + self.speedY >= 500:
                # print("2")
                self.speedY = -self.speedY
        else:
            if y - 12 - self.speedY <= 0:
                # print("12")
                self.speedY = -self.speedY

        x += self.speedX
        y += self.speedY
        self.drawMe((x, y))

    def check_collision(self, spriteGroup):
        group.remove(self)
        k = pg.sprite.spritecollide(self, group, False, pg.sprite.collide_circle)
        if k:
            for j in k:
                speed_after_collision(j, self)
        group.add(self)


def speed_after_collision(obstacle, ball):
    y_obstacle_center = obstacle.center[1]
    x_obstacle_center = obstacle.center[0]
    y_ball_center = ball.center[1]
    x_ball_center = ball.center[0]

    if ball.speedX:
        angle_ball_and_x = math.atan(ball.speedY / ball.speedX)
    else:
        neg = 1
        if ball.speedY < 0:
            neg = -1
            angle_ball_and_x = 1.5708 * neg
        elif ball.speedY > 0:
            angle_ball_and_x = 1.5708 * neg
        else:
            angle_ball_and_x = 0

    print(obstacle.speedX,"yes")

    if obstacle.speedX:
        angle_obstacle_and_x = math.atan(obstacle.speedY / obstacle.speedX)
    else:
        neg = 1
        if obstacle.speedY < 0:
            neg = -1
            angle_obstacle_and_x = 1.5708 * neg
        elif obstacle.speedY > 0:
            angle_obstacle_and_x = 1.5708 * neg
        else:
            angle_obstacle_and_x = 0

    angle_centres_and_x = math.atan((y_obstacle_center - y_ball_center)/(x_obstacle_center - x_ball_center))
    angle_ball_obs = abs(angle_centres_and_x - angle_ball_and_x)
    angle_obs_ball = abs(angle_centres_and_x - angle_obstacle_and_x)

    ball_velocity = math.sqrt(ball.speedX ** 2 + ball.speedY ** 2)
    obstacle_velocity = math.sqrt(obstacle.speedX ** 2 + obstacle.speedY ** 2)

    speedobs_after_hit = ball_velocity * math.cos(angle_ball_obs)
    speedObsx = int(speedobs_after_hit * math.cos(angle_obstacle_and_x))
    speedObsy = int(speedobs_after_hit * math.sin(angle_obstacle_and_x))
    speedball_after_hit = obstacle_velocity * math.cos(angle_obs_ball)
    speedballx = int(speedball_after_hit * math.cos(angle_ball_and_x))
    speedbally = int(speedball_after_hit * math.sin(angle_ball_and_x))

    tempO = (speedObsx, speedObsy)
    obstacle.speedX += (speedObsx - speedballx)
    obstacle.speedY += (speedObsy - speedbally)
    tempO1 = (obstacle.speedX, obstacle.speedY)
    ball.speedX -= (speedObsx + speedballx)
    ball.speedY -= (speedObsy + speedbally)
    tempB1 = (ball.speedX, ball.speedY)
    temp = tempB1


    


def make(coin1):
    # pg.draw.line(win, (255, 0, 0), (1, 0), (1, 500))
    pg.display.update()
# def check_boundaries(striker):


striker = Coin(150, 250, (0, 100, 200))
for i in range(1):
    coin1 = Coin(250, 250)




while isRun:
    pg.time.delay(40)
    win.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRun = False

    for i in group:
        i.updateX()
    # coin2.updateX()
    make(coin1)
    striker.check_collision(group)


pg.quit()



