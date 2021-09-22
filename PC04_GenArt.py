"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Maggie Perry

********* HEY, READ THIS FIRST **********

This code creates a pattern of circles that make up a larger shape.
There is a total of 5 of these shapes, each with a different color pallette.
When the code is run, these shapes will show up in different locations in the pannel.


"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================



# define variables
locations = [(-200,200), (-200,-200), (200,-200), (200,200), (150,-50), (-150,-50), (150,50),
             (150,-50), (100,0), (0,100), (-100,0), (0,-100), (0,0), (50,50), (-50,-50)]
bPalette = [(0,128,128), (0,255,255), (0,206,209), (64,224,209), (100,149,237), (0,191,255),
            (30,144,255), (135,206,250), (0,0,139), (0,0,255), (65,105,225), (173,216,230)]
rPalette = [(128,0,0), (178,34,34), (220,20,60), (255,0,0), (255,99,71), (255,127,80), 
            (205,92,92), (240,128,128), (255,69,0), (255,140,0), (255,215,0), (218,165,32)]
gPalette = [(154,205,50), (85,107,47), (107,142,35), (127,255,0), (173,255,47), (0,100,0),
            (34,139,34), (0,255,0), (144,238,133), (152,251,152), (143,188,143),
            (46,139,87)]
pPalette = [(221,160,221), (238,130,238), (255,0,255), (218,112,214), (199,21,133), (255,153,255),
            (219,112,147), (255,20,147), (255,204,255),(255,182,193), (250,128,114), (255,0,127)]
lPalette = [(138,43,226), (75,0,130), (72,61,139), (106,90,205), (123,104,238), (147,112,219),
            (139,0,139), (148,0,211), (153,50,204), (186,85,211), (128,0,128), (216,191,216)]
radius = 50

# blue turtle
bt = turtle.Turtle()
bt.speed(20)
bt.pensize(2)

bt.penup()
#randomly selects a start location from above list of coordinates
bt.goto(random.choice(locations)) 
bt.pendown()
# this loop creates 60 small blue circles that rotate around to make a larger one
for b in range(60): 
    bt.pencolor(random.choice(bPalette)) #randomluy selects a color from above palette
    bt.circle(radius)
    bt.left(6)

# red turtle
rt = turtle.Turtle()
rt.speed(20)
rt.pensize(2)

rt.penup()
#randomly selects a start location from above list of coordinates
rt.goto(random.choice(locations))
rt.pendown()
# this loop creates 60 small red circles that rotate around to make a larger one
for r in range(60):
    rt.pencolor(random.choice(rPalette)) #randomluy selects a color from above palette
    rt.circle(radius)
    rt.left(6)
    
# green turtle
gt = turtle.Turtle()
gt.speed(20)
gt.pensize(2)

gt.penup()
#randomly selects a start location from above list of coordinates
gt.goto(random.choice(locations))
gt.pendown()
# this loop creates 60 small green circles that rotate around to make a larger one
for g in range(60):
   gt.pencolor(random.choice(gPalette)) #randomluy selects a color from above palette
   gt.circle(radius)
   gt.left(6)

# pink turtle
pt = turtle.Turtle()
pt.speed(20)
pt.pensize(2)

pt.penup()
#randomly selects a start location from above list of coordinates
pt.goto(random.choice(locations))
pt.pendown()
# this loop creates 60 small pink circles that rotate around to make a larger one
for p in range(60):
   pt.pencolor(random.choice(pPalette)) #randomluy selects a color from above palette
   pt.circle(radius)
   pt.left(6)

# purple turtle
lt = turtle.Turtle()
lt.speed(20)
lt.pensize(2)

lt.penup()
#randomly selects a start location from above list of coordinates
lt.goto(random.choice(locations))
lt.pendown()
# this loop creates 60 small purple circles that rotate around to make a larger one
for l in range(60):
   lt.pencolor(random.choice(lPalette)) #randomluy selects a color from above palette
   lt.circle(radius)
   lt.left(6)


# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
