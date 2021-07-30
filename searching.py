from turtle import Shape, Screen, Turtle, Vec2D as Vec
import random
import threading
from threading import Thread
motion_accept = False

# Creates a turtle object with turtle shape.
copter_right = 'helicopter_right.gif'
copter_left = 'helicopter_left.gif'
seaman_img = 'seaman.gif'

copter = Turtle('turtle')
sailor = Turtle('turtle')


def forward(steps, direction):
    global motion_accept
    for step in range(steps):
        if motion_accept:
            if direction == 'right':
                copter.shape(copter_right)
            elif direction == 'left':
                copter.shape(copter_left)
            copter.fd(1)
            if searching():
                motion_accept = False
                break




def turn(direction):
    if motion_accept:
        if direction == 'right':
            copter.right(90)
        elif direction == 'left':
            copter.left(90)


def copter_movement():
    global motion_accept
    motion_accept = True
    for loop_number in range(13):
        if motion_accept:
            forward(600, 'right')
            turn('right')
            forward(20, 'right')
            turn('right')
            forward(600, 'left')
            turn('left')
            forward(20, 'right')
            turn('left')


def searching():
    distanse_to_sailor = copter.pos() - sailor.pos()
    #print(abs(distanse_to_sailor[0]))
    if abs(distanse_to_sailor[0]) <= 20 and abs(distanse_to_sailor[1]) <= 20:
        copter.write("Sailor found!", font=("Arial", 16, "normal"))
        return True
    else:
        return False


def main():
    screen = Screen()
    screen.setup(width=1.0, height=1.0)  # For fullscreen.
    #screen.bgcolor('black')
    screen.title("Seaching")

    screen.register_shape(copter_right)
    screen.register_shape(copter_left)
    screen.register_shape(seaman_img)

    copter.pencolor('red')
    copter.shape(copter_right)
    sailor.shape(seaman_img)
    sailor.penup()
    sailor.setpos(random.randint(-300, 300), random.randint(-250, 250))
    sailor_stamp = sailor.stamp()

    # copter movement
    copter.penup()
    copter.setpos(-300, 250)
    copter.pendown()

    copter_movement()
    #searching_thread = Thread(target=searching())
    #searching_thread.start()
    #movement_thread = Thread(target=copter_movement())





if __name__ == '__main__':
    main()
