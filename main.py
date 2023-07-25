import turtle
import tkinter.messagebox
import fire_simulation as fs
import forest_fire as f


def stop_simulation(callback):
    answer = tkinter.messagebox.askyesno(
        'Animated scene', "Do you want to see the animated version of the simulation?")
    print('answer:', answer)

    if answer:
        callback()
    else:
        turtle.bye()


def animated_scene(x=0, y=0):
    turtle.clearscreen()
    turtle.reset()
    f.simulation()


def first_scene(x=0, y=0):
    fs.main()
    turtle.onscreenclick(lambda x, y: stop_simulation(animated_scene))


if __name__ == "__main__":
    first_scene()

turtle.mainloop()
