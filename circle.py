from turtle import *

pencolor('white')
pensize(3)
fillcolor('red')
bgcolor('black')

speed('slow')
for i in range(15,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()