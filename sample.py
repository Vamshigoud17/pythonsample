n = int(input("Enter the number of odd prime numbers you want to print: "))
count = 0
num = 3  # Start from 3 because we want odd primes (2 is the only even prime)

while count < n:
    # Check if the number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 2  # Increment by 2 to check only odd numbers (even numbers can't be prime except 2)
