ranks = []

while True:
    user_input = input("Enter rank: ")

    if user_input == "-999":
        if len(ranks) < 10:
            print("Need at least 10 valid ranks. Keep entering.")
            continue
        else:
            break

    try:
        rank = int(user_input)
        if 1 <= rank <= 5:
            ranks.append(rank)
        else:
            print("Not in range, skip")
    except ValueError:
        print("Invalid input, skip")

print(f"Number of valid ranks: {len(ranks)}")
if len(ranks) > 0:
    print(f"Average rank: {sum(ranks) / len(ranks):.2f}")
    print(f"Highest rank: {max(ranks)}")