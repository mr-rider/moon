import turtle

# Creates a turtle object with turtle shape.
steve = turtle.Turtle('turtle')

a_stamp = steve.stamp()
print(steve.position())

steve.fd(150)
steve.color('gray')
a_stamp = steve.stamp()
steve.left(45)
steve.bk(75)
steve.color('black')
steve.setheading(180)
a_stamp = steve.stamp()
steve.pendown()
steve.fd(50)
steve.shape('triangle')
# Moves turtle forward 50 pixels.
steve.fd(50)
# Rotates turtle left 90 degrees.
steve.left(90)
steve.fd(50)
steve.left(90)
steve.fd(50)