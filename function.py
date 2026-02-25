#prime number or not

def is_prime(n):
    if n <= 1:
        print(f'The number is {number} not a prime number')
    for i in range(2, n):
        if n % i == 0:
            print(f'The number is {number} not a prime number')

    print(f'The number is {number}a prime number')

number= int(input('enter a number:'))
is_prime(number)
