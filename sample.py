n = int(input("Enter the number of prime numbers you want to print: "))
count = 0
num = 2

while count < n:
    # Check if the number is prime
    is_prime = True
    for i in range(2, num + 1):  # Check divisibility up to the square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1
