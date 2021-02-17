#  File: Art.py

#  Description: Creates a fractal with squares

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 2/26/2018

#  Date Last Modified: 3/2/2018

import os
import turtle

# draw a line from point p1 to point p2
def drawLine (ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# draw squares recursively
def squares (ttl, order, p, side):

  if (order > 0 and order < 10):
        
    # define the corners of the squares
    p1 = [p[0] - side // 2, p[1] + side // 2]
    p2 = [p[0] - side // 2, p[1] - side // 2]
    p3 = [p[0] + side // 2, p[1] + side // 2]
    p4 = [p[0] + side // 2, p[1] - side // 2]

    #draw the square
    if ( order%2 == 0 ):
        ttl.color('red')
        drawLine (ttl, p1, p2)
        ttl.color('green')
        drawLine (ttl, p2, p4)
        ttl.color('red')
        drawLine (ttl, p4, p3)
        ttl.color('green')
        drawLine (ttl, p3, p1)
    else:
        ttl.color('green')
        drawLine (ttl, p1, p2)
        ttl.color('red')
        drawLine (ttl, p2, p4)
        ttl.color('green')
        drawLine (ttl, p4, p3)
        ttl.color('red')
        drawLine (ttl, p3, p1)

    # recursively draw the squares at the end points
    squares (ttl, order - 1, p1, side // 2)
    squares (ttl, order - 1, p2, side // 2)
    squares (ttl, order - 1, p3, side // 2)
    squares (ttl, order - 1, p4, side // 2)

def main():
  # prompt the user to enter an order for the squares fractal
  print('Recursive Art')
  print()
  order = 0
  while( order<1 or order>9 ):
      order = int (input ('Enter a level of recursion between 1 and 6: '))

  turtle.tracer(10000)
  # put label on top of page
  turtle.title ('Squares')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('red')
  ttl.speed(0)

  # draw the squares
  p = [0, 0]
  squares (ttl, order, p, 300)

  # persist drawing
  ttl.hideturtle()
  
main()
