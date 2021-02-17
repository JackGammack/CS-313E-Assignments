#  File: Geom.py

#  Description: Creates and compares points, rectangles, and circles from geom.txt

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 1/29/2018

#  Date Last Modified: 2/1/2018

import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist(c.center)
    return ( distance < (self.radius + c.radius) )
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    return Circle( r.rad() , r.center().x , r.center().y )

  # string representation of a circle
  def __str__ (self):
    return '(' + str(self.center.x) + ' , ' + str(self.center.y) + ') : ' + str( round( float(self.radius) , 2 ) )
    
  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return abs( self.radius - other.radius ) < tol

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine center of Rectangle
  def center (self):
      c = Point( self.ul.x + self.length()/2 , self.lr.y + self.width()/2 )
      return c

  # determine distance from center to corner
  def rad (self):
      return self.center().dist( self.ul )

  # determine length of Rectangle (distance along the x axis)
  def length (self):
      return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  def width (self):
      return self.ul.y - self.lr.y

  # determine the perimeter
  def perimeter (self):
      return 2*self.length() + 2*self.width()
    
  # determine the area
  def area (self):
      return self.length()*self.width()

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
      return ( p.x > self.ul.x and p.x < self.lr.x and p.y > self.lr.y and p.y < self.lr.y )   

  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
      return ( r.ul.x > self.ul.x and r.lr.x < self.lr.x and r.ul.y < self.ul.y and r.lr.y > self.lr.y )
               
  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
      return not ( self.lr.x < other.ul.x or self.ul.x > other.lr.x or self.ul.y < other.lr.y or self.lr.y > other.ul.y )

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
      return Rectangle( c.center.x - c.radius , c.center.y + c.radius , c.center.x + c.radius , c.center.y - c.radius )
      
  # give string representation of a rectangle
  def __str__ (self):
      return '(' + str(self.ul.x) + ' , ' + str(self.ul.y) + ') : (' + str(self.lr.x) + ' , ' + str(self.lr.y) + ')'

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
      tol = 1.0e-16
      return ( abs(self.length() - other.length()) < tol and abs(self.width() - other.width()) < tol )

def main():
  # open the file geom.txt
  geom = open('geom.txt', 'r')
  # create Point objects P and Q
  pstr = geom.readline().split(' ')
  p = Point( float(pstr[0]) , float(pstr[1]) )
  qstr = geom.readline().split(' ')
  q = Point( float(qstr[0]) , float(qstr[1]) )
  # print the coordinates of the points P and Q
  print('Coordinates of P:', p)
  print('Coordinates of Q:', q)
  # find the distance between the points P and Q
  print( 'Distance between P and Q:' , str( round( float(p.dist(q)) , 2 ) ) )
  # create two Circle objects C and D
  cstr = geom.readline().split(' ')
  c = Circle( float( cstr[2] ) , float( cstr[0] ) , float( cstr[1] ) )
  dstr = geom.readline().split(' ')
  d = Circle( float( dstr[2] ) , float( dstr[0] ) , float( dstr[1] ) )
  # print C and D
  print( 'Circle C:' , c )
  print( 'Circle D:' , d )
  # compute the circumference of C
  print( 'Circumference of C:' , str( round( float( c.circumference() ) , 2 ) ) )
  # compute the area of D
  print( 'Area of D:' , str( round( float( d.area() ) , 2 ) ) )
  # determine if P is strictly inside C
  if ( c.point_inside(p) ):
      print( 'P is inside C' )
  else:
      print( 'P is not inside C' )
  # determine if C is strictly inside D
  if ( d.circle_inside(c) ):
      print( 'C is inside D' )
  else:
      print( 'C is not inside D' )
  # determine if C and D intersect (non zero area of intersection)
  if ( c.does_intersect(d) ):
      print( 'C does intersect D' )
  else:
      print( 'C does not intersect D' )
  # determine if C and D are equal (have the same radius)
  if ( c == d ):
      print( 'C is equal to D' )
  else:
      print( 'C is not equal to D')
  # create two rectangle objects G and H
  gstr = geom.readline().split(' ')
  g = Rectangle( float(gstr[0]) , float(gstr[1]) , float(gstr[2]) , float(gstr[3]) )
  hstr = geom.readline().split(' ')
  h = Rectangle( float(hstr[0]) , float(hstr[1]) , float(hstr[2]) , float(hstr[3]) )  
  # print the two rectangles G and H
  print( 'Rectangle G:' , g )
  print( 'Rectangle H:' , h )
  # determine the length of G (distance along x axis)
  print( 'Length of G:' , str(g.length()) )
  # determine the width of H (distance along y axis)
  print( 'Width of H:' , str(h.width()) )
  # determine the perimeter of G
  print( 'Perimeter of G:' , str(g.perimeter()) )
  # determine the area of H
  print( 'Area of H:' , str( h.area() ) )
  # determine if point P is strictly inside rectangle G
  if ( g.point_inside( p ) ):
      print( 'P is inside G' )
  else:
      print( 'P is not inside G')
  # determine if rectangle G is strictly inside rectangle H
  if ( h.rectangle_inside( g ) ):
      print( 'G is inside H' )
  else:
      print( 'G is not inside H' )
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if ( g.does_intersect(h) ):
      print( 'G does overlap H' )
  else:
      print( 'G does not overlap H' )
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  cc = Circle()
  print( 'Circle that circumscribes G:' , cc.circle_circumscribes( g ) )
  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  rc = Rectangle()
  print( 'Rectangle that circumscribes D:' , rc.rect_circumscribe( d ) )
  # determine if the two rectangles have the same length and width
  if ( g == h ):
      print( 'Rectangle G is equal to H' )
  else:
      print( 'Rectangle G is not equal to H' )
  # close the file geom.txt
  geom.close()
main()
