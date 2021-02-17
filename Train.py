#  File: Train.py

#  Description: Draws a train using Turtle Graphics

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 2/9/2018

#  Date Last Modified: 2/14/2018

import turtle, math

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)

def drawRect (ttl,x,y,width,height):
    ttl.penup()
    ttl.goto(x,y)
    ttl.pendown()
    for i in range(2):
        ttl.forward(width)
        ttl.left(90)
        ttl.forward(height)
        ttl.left(90)

def drawCircle(ttl,x,y,rad):
    ttl.penup()
    ttl.goto(x,y)
    ttl.pendown()
    ttl.circle(rad)

def draw_wheels(ttl, x, y, larger_r, smaller_r):
	inc = turtle.Turtle()
	inc.speed(10000)
	inc.penup()
	inc.goto(x, y + larger_r - smaller_r)

	inc.color('red')
	ttl.color('red')
	
	ttl.penup()
	ttl.setheading(0)
	
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(larger_r)
	ttl.penup()

        
	spoke_angle = 5
	for r in range(2):
		for q in range(9):
			inc.goto(x, y + larger_r - smaller_r)
			inc.pendown()
			inc.circle(smaller_r, q * 45)
			ttl.goto(x, y + smaller_r)
			ttl.pendown()
			ttl.circle(larger_r - smaller_r, spoke_angle)
			ttl.goto(inc.position())
			inc.penup()
			ttl.penup()
			spoke_angle += 45
			inc.setheading(0)
			ttl.setheading(0)
		spoke_angle = -5

	inc.ht()
	ttl.ht()
        
        
def main():
    turtle.setup(800,800,0,0)
    ttl = turtle.Turtle()
    ttl.color('black')
    ttl.speed(10000)
    ttl.width(2)

    #Tracks
    drawLine(ttl,-300,-200,410,-200)
    drawLine(ttl,-300,-210,410,-210)
    i=-295
    while( i<390 ):
      drawRect(ttl,i,-215,15,5)
      i+=40   

    #Wheels
    ttl.color('red')
    draw_wheels(ttl,-200,-200,50,40)
    draw_wheels(ttl,0,-200,45,35)
    draw_wheels(ttl,200,-200,45,35)

    #Left and Bottom of train and grill
    ttl.color('blue')
    drawLine(ttl,-280,-140,-260,-140)
    drawLine(ttl,-280,-140,-280,100)
    drawLine(ttl,-280,100,-110,100)
    drawLine(ttl,-110,100,-110,-140)
    drawLine(ttl,-110,-140,-140,-140)
    ttl.pendown()
    ttl.left(90)
    ttl.circle(60,180)
    drawLine(ttl,-140,-140,-50,-140)
    ttl.left(180)
    ttl.pendown()
    ttl.circle(-50,180)
    drawLine(ttl,50,-140,150,-140)
    ttl.left(180)
    ttl.pendown()
    ttl.circle(-50,180)
    drawLine(ttl,250,-140,280,-140)
    ttl.pendown()
    ttl.left(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(20)
    ttl.left(90)
    ttl.forward(70)
    ttl.left(115)
    ttl.forward(70)
    ttl.right(25)
    drawLine(ttl,ttl.xcor(),ttl.ycor(),290,ttl.ycor())
    drawLine(ttl,290,ttl.ycor(),290,-140)
                    
    #Right side of train
    ttl.pendown()
    ttl.forward(190)
    ttl.left(90)
    ttl.forward(400)
    drawLine(ttl,-110,100,-90,100)
    drawLine(ttl,-90,100,-90,110)
    ttl.pendown()
    ttl.forward(210)
    ttl.left(90)
    ttl.forward(10)
    ttl.left(90)
    ttl.forward(20)

    #Windows
    ttl.fillcolor ("#BEBEBE")
    ttl.begin_fill()
    drawRect(ttl,-265,-10,60,80)
    ttl.end_fill()
    ttl.fillcolor ("#BEBEBE")
    ttl.begin_fill()
    drawRect(ttl,-185,-10,60,80)
    ttl.end_fill()

    #Top features
    ttl.penup()
    ttl.goto(290,-140)
    ttl.pendown()
    ttl.left(90)
    ttl.forward(60)
    ttl.right(90)
    ttl.forward(20)
    ttl.left(90)
    ttl.forward(80)
    ttl.right(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(50)
    ttl.right(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(80)
    ttl.left(90)
    ttl.forward(20)
    ttl.right(90)
    ttl.forward(20)
    ttl.left(90)

    #right smoke stack
    ttl.forward(75)
    ttl.right(110)
    ttl.forward(70)
    ttl.left(40)
    ttl.forward(20)
    ttl.left(70)
    ttl.forward(70)
    ttl.left(70)
    ttl.forward(20)
    ttl.left(110)
    ttl.forward(83)
    ttl.left(180)
    ttl.forward(83)
    ttl.left(110)
    ttl.forward(70)
    ttl.right(110)
    ttl.forward(110)

    #left smoke stack
    ttl.right(90)
    ttl.forward(25)
    ttl.left(90)
    ttl.forward(15)
    ttl.right(90)
    ttl.forward(10)
    ttl.left(90)
    ttl.forward(30)
    ttl.left(90)
    ttl.forward(10)
    ttl.left(90)
    ttl.forward(30)
    ttl.left(180)
    ttl.forward(45)
    ttl.left(90)
    ttl.forward(25)

    #middle stripe
    ttl.penup()
    ttl.goto(-110,-30)
    ttl.pendown()
    ttl.left(90)
    ttl.forward(400)
    ttl.right(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(400)

    #right stripe
    ttl.penup()
    ttl.goto(205,50)
    ttl.pendown()
    ttl.left(90)
    ttl.forward(80)
    ttl.right(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(80)
    ttl.left(90)
    ttl.forward(195)

    #left stripe
    ttl.left(90)
    ttl.forward(80)
    ttl.right(90)
    ttl.forward(10)
    ttl.right(90)
    ttl.forward(80)
    
    #middle dots
    ttl.penup()
    ttl.color('black')
    ttl.right(90)
    ttl.goto(-105,-35)
    while( ttl.xcor()<290 ):
      ttl.dot(6)
      ttl.forward(8)

    #right dots
    ttl.goto(200,45)
    ttl.right(90)
    while( ttl.ycor()>-30 ):
      ttl.dot(6)
      ttl.forward(8)

    #left dots
    ttl.goto(-5,45)
    while( ttl.ycor()>-30 ):
      ttl.dot(6)
      ttl.forward(8)

    
    

main()
