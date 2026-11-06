strings_entered = []

while True:
    user_input = input("Enter string: ")
    if user_input == "quit":
        break
    strings_entered.append(user_input)

found_match = False
for s in strings_entered:
    if s[::-1] in strings_entered:
        found_match = True
        break
if found_match:
    print("Reversed match found")
else:
    print("No reversed match found")
