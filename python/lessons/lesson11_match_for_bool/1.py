from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
def main():
    # Ask the user for a whole number volume level
    user_input = input("Enter a volume level (1-10): ")

    try:
        # Convert the input to a whole number (integer)
        volume = int(user_input)

        # Match the volume level to its description
        match volume:
            case 1 | 2:
                print("Faint / Very Quiet")
            case 3 | 4:
                print("Quiet / Comfortable")
            case 5 | 6:
                print("Moderate / Medium")
            case 7 | 8:
                print("Loud / High")
            case 9 | 10:
                print("Very Loud / Maximum")
            case _:
                print("Invalid volume level! Please enter a number between 1 and 10.")

    except ValueError:
        # Handle cases where the user inputs text instead of a whole number
        print("Error: Please enter a valid whole number.")


if __name__ == "__main__":
    main()
stop()