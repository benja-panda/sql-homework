from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
number = 0
total_sum = 0

while True:
    try:
        number= int(input("enter a number up to 999: "))
        if number==999:
            break
        total_sum= total_sum + number
    except ValueError:
        print("enter a valid number")
print("total:",total_sum)
stop()