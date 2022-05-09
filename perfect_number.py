# A perfect number is a number for which the sum of its proper divisors 
# is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors 
# is less than n and it is called abundant if this sum exceeds n.

# This program determines if a given number is perfect, abundant, or deficient


from utility import proper_divisors

print("Hello! This program will tell you if a number is perfect, abundant or deficient.")
number = int(input("Enter a number: "))

divisors = proper_divisors(number)
sum_divisors = sum(divisors)

# The number is perfect
if sum_divisors == number:
    print(f"{number} is a perfect number!")
    print(f"{divisors} sum up to {sum_divisors}, and {number} = {sum_divisors}")
elif sum_divisors > number:
    print(f"{number} is an abundant number!")
    print(f"{divisors} sum up to {sum_divisors}, and {sum_divisors} > {number}")
else:
    print(f"{number} is a deficient number!")
    print(f"{divisors} sum up to {sum_divisors}, and {sum_divisors} < {number}")
