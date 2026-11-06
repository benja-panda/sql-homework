
def circle_area(radius):
    """Calculates the area of a circle.

    :param radius: The radius of the circle
    :return: The calculated area as a float
    """
    return 3.14 * radius**2

print(circle_area(1))
print(circle_area(2.5))
print(circle_area(radius=10))

#########
def is_adult(age=0):
    """Checks if the given age qualifies as an adult.

    :param age: The age to check, defaults to 0
    :return: True if age is 18 or older, False otherwise
    """
    return age >= 18

print(is_adult())
print(is_adult(17))
print(is_adult(18))
print(is_adult(age=40))
##########

def apply_discount(price, percent=10):
    """Applies a percentage discount to a given price.

    :param price: The original price
    :param percent: The discount percentage, defaults to 10
    :return: The discounted price as a float
    """
    return price - (price * (percent / 100))
print(apply_discount(200))
print(apply_discount(200, 25))
print(apply_discount(200, percent=50))
print(apply_discount(price=80, percent=5))

##########

def count_vowels(text):
    """Counts the number of vowels in a string.

    :param text: The string to check for vowels
    :return: The total count of vowels found
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("incognito"))
print(count_vowels("missiiiissippi"))
print(count_vowels("xyz"))


