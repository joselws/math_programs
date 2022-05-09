# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Determine whether a given number is amicable and also determine its pair

from utility import proper_divisors

a = int(input("Enter a number, this program will determine whether it's an amicable number and its pair, if it has one: "))

a_divisors = proper_divisors(a)
sum_a_divisors = sum(a_divisors)

b = sum_a_divisors
b_divisors = proper_divisors(b)
sum_b_divisors = sum(b_divisors)

# Numbers are amicable and a is not b
if a == sum_b_divisors and a != b:
    print(f"The number {a} is amicable! its divisors are: {a_divisors},")
    print(f"which summed up equals {sum_a_divisors}")
    print(f"and its amicable pair is {b}! its divisors are: {b_divisors},")
    print(f"which summed up equals {sum_b_divisors}")
else:
    print(f"{a} is not an amicable number!")