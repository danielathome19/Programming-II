from turtle import *

speed('fastest')
rt(-90)
angle = 30

def y(sz, level):
  if level > 0:
    fd(sz)
    rt(angle)
    y(0.8 * sz, level-1)
    lt(2*angle)
    y(0.8*sz, level-1)
    rt(angle)
    fd(-sz)
    
y(80, 7)
done()