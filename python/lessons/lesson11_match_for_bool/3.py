from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
def main():
    # Ask the user for the service time and meal price
    minutes = float(input("How many minutes did the meal take? "))
    price = float(input("How much did it cost (in shekels)? "))

    # Build the boolean variables based on the criteria
    is_quick_service = minutes < 15
    is_expensive = price > 100

    # Decide and print the recommendation based on the booleans
    if is_quick_service and not is_expensive:
        print("recommended")
    else:
        print("not recommended")

if __name__ == "__main__":
    main()
stop()