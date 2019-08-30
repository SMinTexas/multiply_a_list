# Given a list of numbers, and a single factor (also a number), create a
# new list consisting of each of the numbers in the first list multiplied by
# the factor.  Print this list.

mult_factor = 2
numbers = [2,4,6,8,10]
new_numbers = []

for number in numbers:
    product = number * mult_factor
    new_numbers.append(product)

print(new_numbers)