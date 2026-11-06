from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
grade=int(input('Enter your grade: '))

if grade <=100 and grade>=0:
    print("valid grade")
else:

    print("invalid grade")
stop()
