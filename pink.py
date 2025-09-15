from turtle import *
bgcolor('black')
speed(100)
color('cyan','pink')
begin_fill()
for x in range(900):
	circle(180,200)
	if x%10==0:
		circle(70,90)
end_fill()
done()	