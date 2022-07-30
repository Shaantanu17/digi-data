from turtle import *

speed('fast')
bgcolor('white')
pencolor('black')

fillcolor('grey')
begin_fill()

for i in range(200):
    fd(i)
    lt(90)

    end_fill()
    mainloop()
