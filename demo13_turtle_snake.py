import turtle
import random
from freegames import vector,square
from random import randrange
import time

#
turtle.setup(700, 400, 200, 200)
turtle.home()
turtle.pendown()
turtle.delay(delay=0)
turtle.speed(100)
turtle.ht()
turtle.pensize(5)

# global parameters
global Blocks_xlist,Blocks_ylist,food_xlist,food_ylist,foodCount,count,num_Blocks
Blocks_xlist=[]
Blocks_ylist=[]
food_xlist=[]
food_ylist=[]
foodCount = 4
count=0
num_Blocks=3

class Blocks():
    def __init__():
        self.count=None
    
    def generate():
        global Blocks_xlist,Blocks_ylist
        x = randrange(-15,0)*10
        y = randrange(-15,0)*10
        Blocks_xlist.append(x)
        Blocks_ylist.append(y)
        square(x, y, 20, 'black')

class food():
    def __init__():
        self.count=None
    
    def generate():
        global food_xlist,food_ylist
        x=randrange(1, 15) * 10
        y=randrange(1, 15) * 10
        square(x, y, 3, 'red')
        food_xlist.append(x)
        food_ylist.append(y)

class Snake():
    def __init__(self,n,color):
        self.n=n
        self.eatFoodCount = 0
        self.body=self.initialize()
        self.color=color
        
    def initialize(self):
        body=[]        
        body.append(turtle.pos())
        for _ in range(self.n):
            turtle.fd(10)
            body.append(turtle.pos())
        self.heading=turtle.heading()
        return body

    def erase_tail(self):
        # draw head and erase tail
        # penup
        turtle.penup()
        turtle.goto(self.body[0])
        # pendown
        turtle.color('white')
        turtle.pendown()
        # erase
        turtle.goto(self.body[1])
        # draw and recover
        turtle.penup()
        turtle.color(self.color)
        turtle.goto(self.body[self.n])
        turtle.seth(self.heading)
        turtle.pendown()
        for i in range(self.n):
            self.body[i]=self.body[i+1]
    
    def whereToGo(self):
        heading=self.heading
        headings=[]
        for _ in range(10):
            headings.append(heading+random.uniform(-120, 120))
        return random.choice(headings[:6])
        
    def go_ahead(self):
        h=self.heading+random.uniform(-90, 90)
        turtle.seth(h)
        turtle.penup()
        turtle.fd(10)
        p0=turtle.pos()
        for i in range (0,len(Blocks_xlist)):
            b_x=Blocks_xlist[i]
            b_y=Blocks_ylist[i]
            if abs(p0[0])>=630/2-10 or abs(p0[1])>= 330/2-10 or p0[0]>=b_x-25 and p0[0]<=b_x+25 and p0[1]>=b_y-25 and p0[1]<=b_y+25:
                heading0=turtle.heading()
                h = heading0 + 180      # return to avoid hitting walls
                turtle.seth(h)
                turtle.fd(10)
                p0=turtle.pos()
                print("Enter Danger Zone")
        

        turtle.goto(self.body[self.n])
        turtle.pendown()
        turtle.goto(p0)
        self.body[self.n]=p0   
        self.heading=turtle.heading()

    def test(self):
        x,y=turtle.pos()
        for i in range (0,len(food_xlist)):
            b_x=food_xlist[i]
            b_y=food_ylist[i]
            if x>=b_x-6.5 and x<=b_x+6.5 and y>=b_y-6.5 and y<=b_y+6.5:
                turtle.fillcolor("white")
                turtle.color('white')
                turtle.begin_fill()
                turtle.goto(food_xlist[i],food_ylist[i])
                turtle.fd(4)
                turtle.left(90)
                turtle.fd(4)
                turtle.left(90)
                for j in range(3):
                    turtle.fd(8)
                    turtle.left(90)
                turtle.fd(4)
                turtle.end_fill()
                turtle.color('black')
                global count
                count=count+1
                self.eatFoodCount = self.eatFoodCount+1
                food_xlist[i]=1000
                food_ylist[i]=1000


if __name__ == '__main__':
    color = input('Input color of snakes：')
    color_list = color.split(' ')
    # Initialize snakes
    snake_list = []
    for i in range(len(color_list)):
        snake_list.append(Snake(5,color_list[i]))
    # Initialize Blocks
    for i in range(num_Blocks):
        Blocks.generate()
    # Initialize Foods
    for i in range(foodCount):
        food.generate()
    
    i=0
    while (count < foodCount) and i<1000:# end till food end， or end till exceed 1000 iterations
        for i in range(len(color_list)):
            snake_list[i].erase_tail()
            snake_list[i].go_ahead()
            snake_list[i].test()
        
        i+=1
    ## Print case for each snake
    for i in range(len(color_list)):
        print("Snake "+ snake_list[i].color + " eats " +  str(snake_list[i].eatFoodCount ) + " foods" )

    # Final Winner
    maxCount  = snake_list[0].eatFoodCount
    maxColor  =  snake_list[0].color
    for i in range(1,len(color_list)):
        if snake_list[i].eatFoodCount > maxCount:
            maxCount =  snake_list[i].eatFoodCount
            maxColor  =  snake_list[i].color
    # Print
    print ("Eat MAXIMUM snake is " + str(maxColor) )

    turtle.done()
