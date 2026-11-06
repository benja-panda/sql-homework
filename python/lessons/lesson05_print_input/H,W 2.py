from tkinter import colorchooser
from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
print("what is your favorite color?")
favorite_color: str=input()
print(favorite_color+" is a beautiful color!")
stop()