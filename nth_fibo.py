# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144

# Determine the nth term of the fibonacci sequence

fibo_term = 2       # keeps track of the current fibo term
current_fibo = 1
previous_fibo = 1

print("Hello! This program will determine the nth term of the fibonacci sequence")
nth_term = int(input("Please enter a number: "))

# Keep getting increased fibo numbers until we reach the desired term
while fibo_term < nth_term:
    fibo_term += 1
    temp = current_fibo
    current_fibo += previous_fibo
    previous_fibo = temp


print(f"The fibonacci number corresponding the term #{nth_term} is {current_fibo}")