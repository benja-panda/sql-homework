from turtledemo.penrose import start
from turtledemo.round_dance import stop
start()
words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

print("All uppercase:", all(w.isupper() for w in words))

print("Has a long word:", any(len(w) > 5 for w in words))

print("By length:", sorted(words, key=len))
stop()