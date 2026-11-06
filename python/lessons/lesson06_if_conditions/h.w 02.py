from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
number=int(input("enter your number?"))
if number<10 and number>99:
    print("number should be between 10 and 99")
else:
    ones= number % 10
    tens= number //10
    if ones==tens:
        print("tens are equal")
    else:
        print("tens are not equal")
stop()