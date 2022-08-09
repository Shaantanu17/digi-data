from turtle import *

pencolor('white')
pensize(2)
fillcolor('red')
bgcolor('black')

speed('fast')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()
