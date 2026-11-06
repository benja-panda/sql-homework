from turtledemo.penrose import start
from turtledemo.round_dance import stop
start()
temps: list[int] = [21, 30, -999, 26, -999, 17, 33, -999, 28]

print("Count:", len(temps))

print("First three:", temps[0:3])
print("Last three:", temps[-3:])

print("Every second:", temps[::2])

while -999 in temps:
    temps.remove(-999)
print("Cleaned:", temps)


print("Dropped the first reading:", temps.pop(0))
temps.append(31)
print("After append:", temps)

total = sum(temps)
count = len(temps)
avg = total / count

print(    f"Max: {max(temps)}  Min: {min(temps)}  Sum: {total}  Avg: {avg:.2f}")

for t in temps:
    if t > avg:
        print("Above average:", t)
stop()