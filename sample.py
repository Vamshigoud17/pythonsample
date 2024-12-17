n = int(input("Enter the number of prime numbers you want to print: "))
count = 0
num = 2
while count < n:
    # Check if the number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1
