# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:06:27 2023

@author: varun
"""

import turtle
import math


var=turtle.Turtle()
turtle.pensize(100)

var.color("red","yellow")
var.speed(10)

var.begin_fill()
for i in range(100):
    var.forward(math.sqrt(i)*10)
    var.left(170)
    
var.end_fill()

turtle.done()