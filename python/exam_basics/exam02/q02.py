def special_percentile(percent: int, numbers: list) -> float:
    sorted_nums = sorted(numbers)
    index = (percent * len(sorted_nums)) // 100
    return float(sorted_nums[index])

#######test
print(special_percentile(25, [50, 10, 40, 30, 20]))