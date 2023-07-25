
import random
import turtle_interpreter
import lsystem
import pygame as pg


def simulation():
    '''
    Test the ability of the TurtleInterpreter to draw trees.
    The program expects the name of an L-system filename (systemF.txt) and then
    draws several trees in the screen, using 6 iterations
    of the rule to generate the string.
    If the TurtleInterpreter draws leaves using the L symbol, then
    the program also draws piles of leaves at the base of each tree.
    '''

    tree = lsystem.Lsystem('systemF.txt')

    sx = 600
    sy = 500
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)
    terp.land(-300, 0, 600)
    terp.sun(-230, 200, 40)

    N = 12

    y_init = -300
    x_init = -200
    while y_init < 200:

        for i in range(N):
            tstr = tree.buildString(6)

            terp.setColor("forestgreen")
            terp.place(x_init, y_init, random.randint(85, 95))
            terp.drawString(tstr, random.randint(2, 4),
                            random.randint(18, 30) * random.choice([1, -1]))

            x_init += 40

        y_init += 30
        x_init -= 400
        terp.hold()


if __name__ == "__main__":
    simulation()
    pg.mixer.music.pause()
