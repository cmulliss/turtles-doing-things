from turtle import *

shape('turtle')
mode('logo')
color('blue', 'red')
begin_fill()
while True:
        forward(180)
        left(160)
        if abs(pos()) < 1:
            break
end_fill()
done()
