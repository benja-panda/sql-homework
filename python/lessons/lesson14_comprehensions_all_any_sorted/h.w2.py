from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
battery: list[int] = [78, 92, 45, 61, 88, 30]

print("All above 20:", all(b > 20 for b in battery))

print("Any below 40:", any(b < 40 for b in battery))

print("All full:", all(b == 100 for b in battery))

ordered = sorted(battery)
print("Ordered:", ordered)
print("Original:", battery)

battery.sort(reverse=True)
print("Sorted desc:", battery)

print("Top three:", battery[:3])
stop()