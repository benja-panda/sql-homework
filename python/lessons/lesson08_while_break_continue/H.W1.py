from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
low_rate = 0
medium_rate = 0
high_rate = 0
valid_ratings = 0


while True:
    #ask for input
    user_input = input("movie rating?")


    score = int(user_input)
    #create break
    if score == -1:
        break

    if score < 1 or score > 5:
        continue

    valid_ratings += 1

    if score == 1 or score == 2:
        low_rate += 1
    elif score == 3:
        medium_rate += 1
    elif score == 4 or score == 5:
        high_rate += 1

print(f"Low (1-2): {low_rate}")
print(f"Medium (3): {medium_rate}")
print(f"High (4-5): {high_rate}")
print(f"Valid ratings: {valid_ratings}")
stop()