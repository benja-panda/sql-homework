night_shift = {"Alex", "Jordan", "Taylor", "Casey"}
access_server_room = {"Jordan", "Casey", "Morgan", "Riley"}
hardware_expert = {"Taylor", "Riley", "Casey", "Alex"}
management_role = {"Jordan", "Morgan"}

print("Clues:")
print("1) The suspect was on the NIGHT SHIFT.")
print("2) The suspect has access to the SERVER ROOM.")
print("3) The suspect is a HARDWARE EXPERT.")
print("4) The suspect is NOT in a MANAGEMENT ROLE.")

guilty = (night_shift) & (access_server_room) & (hardware_expert) - (management_role)

print(guilty)
print(len(guilty))
print(guilty <= night_shift)