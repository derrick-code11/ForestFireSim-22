from gtts import gTTS
import pygame as pg
import turtle
import random


class ForestFire:
    def __init__(self):
        turtle.title('Forest Fire Simulation 2022')
        self.oak = []  # a list of all the oak trees in the forest
        self.fires = []  # a list of all the fires in the forest
        self.pine = []  # a list of all the pine trees in the forest

    def add_oak(self, x, y, tree_color="forest green"):
        '''Create a new oak tree object and add it to the list of oak trees'''
        new_tree = turtle.Turtle()
        new_tree.speed(0)
        new_tree.color(tree_color)
        new_tree.shape("circle")
        new_tree.shapesize(0.65)
        new_tree.settiltangle(90)
        new_tree.penup()
        new_tree.goto(x, y)
        self.oak.append(new_tree)

    def add_pine(self, x, y, tree_color="forest green"):
        '''Create a new pine tree object and add it to the list of pine trees'''
        new_tree = turtle.Turtle()
        new_tree.speed(0)
        new_tree.color(tree_color)
        new_tree.shape("triangle")
        new_tree.shapesize(0.65)
        new_tree.settiltangle(90)
        new_tree.penup()
        new_tree.goto(x, y)
        self.pine.append(new_tree)

    def add_fire(self, x, y, fire_color="red"):
        '''Create a new fire object and add it to the list of fires'''
        new_fire = turtle.Turtle()
        new_fire.speed(0)
        new_fire.color(fire_color)
        new_fire.shape("circle")
        new_fire.shapesize(0.65)
        new_fire.penup()
        new_fire.goto(x, y)
        self.fires.append(new_fire)

    def spread_fire(self):
        '''Move each fire to a random neighboring tree and set it on fire'''

        for fire in self.fires:
            neighbors = [(fire.xcor()+20, fire.ycor()), (fire.xcor()-20, fire.ycor()),
                         (fire.xcor(), fire.ycor()+20), (fire.xcor(), fire.ycor()-20)]

            # Choose a random neighbor to move the fire to
            new_position = random.choice(neighbors)
            fire.goto(new_position)

            # Set the oak tree at the new position on fire
            for tree in self.oak:
                if tree.distance(fire) < 15:
                    id = tree.stamp()
                    tree.color("red")
                    self.fires.append(tree)
                    tree.clearstamp(id)
                    self.oak.remove(tree)

            # Set the pine tree at the new position on fire
            for tree in self.pine:
                if tree.distance(fire) < 15:
                    id = tree.stamp()
                    tree.color("red")
                    self.fires.append(tree)
                    tree.clearstamp(id)
                    self.pine.remove(tree)

    def update(self):
        '''Move the fires and spread them to new trees'''
        self.spread_fire()

    def add_info(self, x, y):
        '''Gives a brief information about forest fires'''
        my_turt = turtle.Turtle()
        my_turt.up()
        my_turt.goto(x, y)
        my_turt.down()
        my_turt.write("ForestFireSim 22: A Dynamic Forest Fire Simulation🌍🌳🌲🔥", font=(
            'Tacoma', 20, 'bold'), align='center')
        my_turt.hideturtle()

    def speak_text(self, file_path):
        '''Generate speech using gTTS and play it using pygame'''

        # Read the text from the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Generate speech using gTTS
        tts = gTTS(text=text, lang='en')
        tts.save('speech.mp3')

        # Play the speech using pygame
        pg.mixer.init()
        pg.mixer.music.load('speech.mp3')
        pg.mixer.music.play()


def main():
    '''Create a new forest fire simulation'''
    ff = ForestFire()

    ff.add_info(0, 250)

    # Speak some text about forest fires
    file_path = 'forest_fire_info.txt'
    ff.speak_text(file_path)

    # Add some trees to the forest
    for i in range(-220, 220, 40):
        for j in range(-220, 220, 40):
            ff.add_oak(i, j)
            ff.add_pine(i+20, j+20)

    # Reading the content of 'start.txt'
    with open('start.txt', 'r') as file:
        text = file.read()

    # Generate speech using gTTS
    tts = gTTS(text=text, lang='en')
    tts.save('speech.mp3')

    # Play the speech using pygame
    pg.mixer.init()
    pg.mixer.music.load('speech.mp3')
    pg.mixer.music.play()

    # Add a fire at the center of the forest
    ff.add_fire(0, 0)

    # Update the simulation 30 times
    for i in range(30):
        ff.update()


if __name__ == "__main__":
    main()
