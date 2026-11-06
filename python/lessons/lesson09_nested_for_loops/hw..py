from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
user_input = int(input("table size?: "))
i=user_input
print(f"{' ':4}", end=" ")
for top in range(1, user_input + 1):
    print(f"{top:4}", end=" ")
print()

for i in range(1, user_input + 1, +1):
    print(f"{i:4}", end=" ")

    for j in range(1, user_input + 1, +1):
        print(f"{i * j:4}", end=" ")
    print()
stop()