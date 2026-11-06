from turtledemo.penrose import start
from turtledemo.round_dance import stop
start()
prices: list[int] = [120, 45, 300, 89, 210, 15, 74]

doubled = [p * 2 for p in prices]
print("Doubled:", doubled)

expensive = [p for p in prices if p > 100]
print("Expensive:", expensive)

on_sale = [p - 50 for p in prices if p > 100]
print("On sale:", on_sale)

labels = ["pricey" if p > 100 else "cheap" for p in prices]
print("Labels:", labels)

as_text = [f"{p} NIS" for p in prices]
print("As text:", as_text)
stop()