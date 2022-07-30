from ctypes import sizeof
from turtle import *

size = 60
side = 20

pencolor('blue')
pensize(3)
speed('fastest')
fillcolor('blue')

for i in range(side):
    forward(size)
    pencolor('red')
    for i in range(side):
        forward(size//5)
        pencolor('green')
        pencolor('black')
        left(360/side)
    left(180/6)    
end_fill('blue')
mainloop()