
import turtle


var=turtle.Turtle()

#first blue color if turtle and another red color is to fill the area
var.color("blue","red")

var.begin_fill() #it is the build in function in python which is impot through the turtle library

var.forward(100)
var.left(90)
var.forward(100)
var.left(90)
var.forward(100)
var.left(90)
var.forward(100)

var.end_fill()

var.penup()
var.forward(150)
var.pendown()


var.begin_fill()
var.forward(100)
var.left(90)
var.forward(100)
var.left(90)
var.forward(100)
var.left(90)
var.forward(100)
var.end_fill()  


turtle.done()

