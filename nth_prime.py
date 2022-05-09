# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# Find the nth prime number


import math

def is_prime(number):
    """Returns true if the number is prime"""
    #Automatically returns true for 2 and 3
    if number == 2 or number == 3:
        return True 

    #Check divisibility by all previous prime numbers found
    for prime in prime_numbers:
        #Optimizing, we only need to test numbers below the square root of the given number
        if prime > int(math.sqrt(number) + 2):
            return True

        #The number is not prime if it's divisible by any of the test numbers
        if number % prime == 0:
            return False

    #If the loop finished without finding any divisible number, then it's prime
    return True


nth_prime = int(input("Choose the nth prime number you wish to find: "))

#this list will hold all prime numbers
prime_numbers = []

count = 0       #amount of prime numbers found
i = 2           #finding numbers from here

#Loop until we find the target prime number
while count < nth_prime:
    #Store the number if it's prime
    if is_prime(i):
        prime_numbers.append(i)
        count += 1

    #Iterate the next number
    i += 1


print(f"The {nth_prime} prime number is {prime_numbers[-1]}")