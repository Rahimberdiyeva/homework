from turtle import*
speed(10)
Screen().bgcolor('black')
screensize(900,700)
penup()
goto(0,100)
pendown()
fillcolor("green")
begin_fill()
left(180)
for _ in range(10):
    forward(7)
    left(-3)
    
for _ in range(20):
    forward(5)
    right(7)

for _ in range(20):
    forward(3)

for _ in range(80):
    forward(2)
    right(1)
    
for _ in range(25):
    forward(2)
    right(1)

for _ in range(20):
    forward(2)
    right(2)
    
for _ in range(25):
    forward(2)
    
for _ in range(25):
    left(1)
    forward(2)
    
for _ in range(20):
    right(-1)
    forward(2)

for _ in range(30):
    left(3)
    forward(3)
right(90)
for _ in range(10):
    right(-4)
    forward(5)
    
right(70)

for _ in range(10):
    left(-3)
    forward(3)

for _ in range(15):
    right(4)
    forward(3)

for _ in range(10):
    right(1)
    forward(2)

for _ in range(30):
    right(0.5)
    forward(2)

for _ in range(10):
    right(2)
    forward(2)

for _ in range(30):
    right(0.3)
    forward(2)

for _ in range(30):
    right(0.8)
    forward(2)

for _ in range(20):
    left(0.5)
    forward(2)

for _ in range(15):
    left(5)
    forward(4)

for _ in range(10):
    right(5)
    forward(3)
end_fill()
####
penup()
goto(40,220)   #+20 -10  goto(30,0)
pendown()
########################
fillcolor("white")
begin_fill()
circle(40)
end_fill()
penup()
goto(100,190)
pendown()
begin_fill()
circle(40)
end_fill()
penup()

goto(12,230)
pendown()
fillcolor("black")
begin_fill()
circle(20)
end_fill()
penup()

goto(72,200)
pendown()
fillcolor("black")
begin_fill()
circle(20)
end_fill()

penup()
goto(100,-170)
pendown()
##################################################
right(120)
fillcolor('#522609')
begin_fill()
left(160)
for _ in range(10):
    right(3)
    forward(3)
for _ in range(10):
    right(4)
    forward(2)
for _ in range(18):
    right(7)
    forward(3)
for _ in range(20):
    left(3)
    forward(1)
for _ in range(30):
    left(1)
    forward(2)

for _ in range(20):
    left(0.5)
    forward(2)
for _ in range(270):
    right(0.5)
    forward(1)

for _ in range(70):
    left(0.5)
    forward(1)

for _ in range(50):
    right(0.5)
    forward(1)

right(20)
for _ in range(50):
    right(1)
    forward(1)
    
right(10)
for _ in range(50):
    right(1)
    forward(1)

for _ in range(70):
    left(0.3)
    forward(1)

for _ in range(70):
    right(0.3)
    forward(1)

for _ in range(70):
    right(0.1)
    forward(1)
    
for _ in range(70):
    left(0.2)
    forward(1)

for _ in range(50):
    right(0.2)
    forward(1)
end_fill()
####################################
pensize(3)
Screen().bgcolor('#A64600')
#fillcolor('#A64600')
penup()
goto(360,-130)  #100 170 40 220
pendown()
begin_fill()
left(160)
for _ in range(6):
    forward(60)
    backward(60)
    right(60)
    forward(60)

exitonclick()