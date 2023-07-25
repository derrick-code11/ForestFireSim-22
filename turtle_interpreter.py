
import turtle
import pygame as pg


class TurtleInterpreter:
    def __init__(self, dx=800, dy=800):
        turtle.bgpic('flames.gif')
        
        pg.mixer.init()
        pg.mixer.music.load('burning.mp3')
        pg.mixer.music.play()

        turtle.bgcolor('#c09655')
        turtle.setup(dx, dy)
        turtle.tracer(False)

    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list   
        of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position
        < : save current color of the turtle
        > : restore the turtle's color
        g : sets turtle's color to green
        y : sets turtle's color to yellow
        r : sets turtle's color to red 
        L : draws a circular leaf
        """

        stack = []
        colorstack = []

        for char in dstring:
            if char == 'F':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append(turtle.position())
                stack.append(turtle.heading())
            elif char == ']':
                turtle.penup()
                turtle.setheading(stack.pop())
                turtle.goto(stack.pop())
                turtle.pendown()

            # modified drawString to handle five additional characters in strings
            elif char == '<':
                colorstack.append(turtle.color()[0])
            elif char == '>':
                new_color = colorstack.pop()
                turtle.color(new_color)
            elif char == 'g':
                turtle.color((0.15, 0.5, 0.2))
            elif char == 'y':
                turtle.color((0.8, 0.8, 0.3))
            elif char == 'r':
                turtle.color((0.7, 0.2, 0.3))
            elif char == 'L':
                turtle.color((0.15, 0.5, 0.2))
                turtle.begin_fill()
                turtle.circle(4, 180)
                turtle.end_fill()
        turtle.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()

    def place(self, xpos, ypos, angle=None):
        '''places the turtle at location (xpos, ypos) and orients the turtle if the angle argument is not None'''
        turtle.penup()
        turtle.goto(xpos, ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.pendown()

    def orient(self, angle):
        '''sets turtle's heading to the given angle.'''
        turtle.setheading(angle)

    def goto(self, xpos, ypos):
        '''send the turtle to (xpos, ypos)'''
        turtle.up()
        turtle.goto(xpos, ypos)
        turtle.down()

    def setColor(self, c):
        '''sets the turtle's color with the argument c.'''
        turtle.color(c)

    def setWidth(self, w):
        '''sets the turtle's width with the argument w.'''
        turtle.width(w)

    def land(self, x, y, dst):
        '''draws a rectangular region to serve as the land'''
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.color('sky blue')
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(dst)
            turtle.left(90)
        turtle.end_fill()

    def sun(self, x, y, rad):
        '''draws a sun in the sky'''
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        turtle.color('yellow')
        turtle.begin_fill()
        turtle.circle(rad)
        turtle.end_fill()
