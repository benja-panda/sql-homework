powers2 = {}
powers3 = {}
powers5 = {}

for i in range(33):
    powers2[2 ** i] = i
    powers3[3 ** i] = i
    powers5[5 ** i] = i

num = int(input("enter a number: "))

if num in powers2:
    print(f"yes 2 power {powers2[num]}")
elif num in powers3:
    print(f"yes 3 power {powers3[num]}")
elif num in powers5:
    print(f"yes 5 power {powers5[num]}")
else:
    print("no")