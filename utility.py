# Several helper functions used throughout my programs

from math import sqrt


def is_prime(number, prime_numbers=[]):
    """Returns True if the number is prime, False otherwise
        it accepts an optional second value which is holds a list of prime numbers"""
    if number == 0 or number == 1:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    # if the list of prime numbers is provided, iterate through it
    if prime_numbers:
        for prime in prime_numbers:
            # No factors exist for those who exceed the square root of the number
            if prime > int(sqrt(number)) + 1:
                return True
            if number % prime == 0:
                return False
            

    # Test every number from 3 to number-1
    else:
        for prime in range(3, number, 2):
            if prime > int(sqrt(number)) + 1:
                return True
            if number % prime == 0:
                return False
    
    # The number is prime if the loop exited without finding a divisible number 
    return True
    

def decompose_prime_factors(number):
    """ Decomposes the number in its prime factors.
    Returns a dictionary where each key is a prime factor
    and each value is each respective prime factor number of occurrences """

    if number < 2:
        print("\nError, this number can't be decomposed!\n")
        return None
    
    # The function will return thisdictionary
    prime_factors_dict = {}

    # There are no prime factors beyond this point
    threshold = int(sqrt(number)) + 1

    # Loop until we have factored the number completely
    while number != 1:

        for i in range(2, number + 1):
            #exit the for loop if we have already factored it completely
            if number == 1:
                break

            #execute if the processing number is a factor of the problem number
            if number % i == 0:
                # Create the existing factor for this number
                prime_factors_dict[i] = 0

                # Loop for as long as the number can be factored by the factor
                while number % i == 0:
                    # Decompose the number and increase factor's occurences
                    number = int( number / i )
                    prime_factors_dict[i] += 1

            # Get the remaining factor value when no other prime factor can be found
            if i > threshold:
                prime_factors_dict[number] = 1
                number = number//number

    return prime_factors_dict


def proper_divisors(number):
    """ Return a list with all divisible numbers of a given number 
        it includes 1 and the number itself """

    # Holds all divisible numbers
    factors = []

    # No factors exist for numbers past its half
    threshold = int(number / 2) + 1

    # Looks for all possible divisible numbers starting at 1
    for i in range(1, threshold):
        if number % i == 0:
            factors.append(i)

    return factors
