import turtle as t
import time
import random as r

wnd=t.Screen()
wnd.title("Snake Game")
wnd.bgcolor("Black")
wnd.tracer()
wnd.setup(720,720)

h=t.Turtle()
h.speed(0)
h.penup()
h.color("white")
h.shape("square")
h.goto(0,0)
h.direction="stop"

food=t.Turtle()
food.speed(0)
food.penup()
food.shape("turtle")
food.color("red")
food.goto(0,100)

def gup():
    if h.direction !='down':
        h.direction="up"
def gdown():
    if h.direction !='up':
        h.direction="down"
def gright():
    if h.direction !='left':
        h.direction="right"
def gleft():
    if h.direction !='right':
        h.direction="left"

def movements():
        if h.direction=='up':
                h.sety(h.ycor() + 20)
        if h.direction=='down':
                h.sety(h.ycor() - 20)
        if h.direction=='right':
                h.setx(h.xcor() + 20)
        if h.direction=='left':
                h.setx(h.xcor() - 20)

bodylist=[]

wnd.listen()
wnd.onkeypress(gup,'Up')
wnd.onkeypress(gdown,'Down')
wnd.onkeypress(gright,'Right')
wnd.onkeypress(gleft,'Left')


while True:
        wnd.update()
        movements()
        time.sleep(0.1)

        if h.xcor()>350 or h.xcor()<-350 or h.ycor()>350 or h.ycor()<-350:
                time.sleep(0)
                h.goto(0,0)
                h.direction="stop"
                for b in bodylist:
                        b.goto(10000,10000)
                bodylist.clear()
                        
        for b in bodylist:
               if b.distance(h) < 20 :
                        time.sleep(0)
                        h.goto(0,0)
                        h.direction="stop"

                        for b in bodylist:
                                b.goto(10000,10000)
                        bodylist.clear()
                        
        if h.distance(food) < 20:
                food.goto(r.randint(-350,350),r.randint(-350,350))
                body=t.Turtle()
                body.shape("circle")
                body.color("white")
                body.penup()
                bodylist.append(body)
                body.speed(0)
               
        for i in range(len(bodylist)-1,0,-1):
                bodylist[i].goto(bodylist[i-1].xcor(),bodylist[i-1].ycor())

        if len(bodylist) > 0:
                bodylist[0].goto(h.xcor(),h.ycor())



wnd.mainloop()
