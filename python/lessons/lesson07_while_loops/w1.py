from turtledemo.penrose import start
from turtledemo.round_dance import stop

start()
number_of_students=int(input("enter number of students"))
i=0
lowest_grade=100
while i<number_of_students:
    grade = int(input("enter grade"))
    i += 1
    if grade>=0:
        if grade<lowest_grade:
            lowest_grade=grade

    else: print("grade cannot be less than 0")

print("the lowest grade is",{lowest_grade})
stop()