# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.

# This program print the collatz sequence of a given number

def collatz(number):
    """ Returns the corresponding next number of the collatz sequence
         of a given number """

    if number % 2 == 0:
        print(f"{number} -> {number}/2 = ", end="")
        next_number = number // 2
    else:
        print(f"{number} -> 3*{number} + 1 = ", end="")
        next_number = 3*number + 1

    print(next_number)
    return next_number


number = int(input("Enter a number, this program will print out its collatz sequence: "))

# Iterates until the sequence finishes
while number != 1:
    number = collatz(number)