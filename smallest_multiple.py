##### Program you will most likely never use #####

# Program that finds the smallest divisible number that can be
# divided from 1 to an user-input number

# For example, if the user inputs 10,
# then 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.


from utility import decompose_prime_factors


print("Welcome! This program shows the minimum number that is divisible \
by 2 up to an user imput.")

number = int(input("Enter a number: "))

# The factors of the number we are looking for
final_number_factors = {}

# Find all factors for all numbers from 2 to that number itself
for i in range(2, number+1):
    # Get its prime factors 
    factors = decompose_prime_factors(i)

    # Iterates every prime factor of it
    for factor in factors:
        # Update final number factors dict
        if factor not in final_number_factors or factors[factor] > final_number_factors[factor]:
            final_number_factors[factor] = factors[factor]


final_number = 1

# Multiply all factors to their respective power together for the final number
for factor, exponent in final_number_factors.items():
    product = factor**exponent
    final_number *= product

print(f"The smallest multiple of all numbers from 1 to {number} is {final_number}")
