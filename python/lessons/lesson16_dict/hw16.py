# 1. Ask the user for four grades
grades = {}
grades['math'] = int(input('math grade: '))
grades['english'] = int(input('english grade: '))
grades['literature'] = int(input('literature grade: '))
grades['python'] = int(input('python grade: '))

print(grades)

# Extract raw grades into a variable first to avoid the trap
raw_grades = list(grades.values())

# 2. Add the average
avg_val = sum(raw_grades) / len(raw_grades)
grades['avg'] = avg_val

# 3. Add the highest and the lowest
max_val = max(raw_grades)
min_val = min(raw_grades)

grades['max'] = max_val
grades['min'] = min_val

print(grades)

# 4. Remove literature from the dictionary
del grades['literature']  # Or: grades.pop('literature')

print(grades)