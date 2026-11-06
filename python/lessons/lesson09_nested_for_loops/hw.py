
from turtledemo.penrose import start
from turtledemo.round_dance import stop


start()
user_input=int(input('how many levels 1-100: '))

for i in range(0, user_input + 1, +1):
    for j in range(0, i, +1):
        print('*', end=" ")
    print()

for i in range( user_input+1, 0 , -1):
    for j in range(0, i, +1):
        print("*", end=" ")
    print()

stop()