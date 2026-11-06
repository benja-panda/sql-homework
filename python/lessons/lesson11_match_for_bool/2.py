from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
import time


def main():
    print("Preparing for launch...")
    time.sleep(1)  # Brief pause before starting the countdown

    # Loop from 5 down to 1 (stops before 0)
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)  # Wait exactly one second before the next number

    # Final launch message after the last second passes
    print("0 - Launch 🚀")


if __name__ == "__main__":
    main()

stop()