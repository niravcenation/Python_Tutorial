# first method
#
# import turtle
# import another_file
#
# hello_number = another_file.another_variable
#
# nirav = turtle.Turtle()
# print(nirav)
# or
#
# from turtle import Turtle,Screen
#
# nirav = Turtle()
# print(nirav)
# nirav.shape("turtle")
# nirav.color("red")
# nirav.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)
