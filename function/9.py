def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primes_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
# start = 10
# end = 50
prime_numbers = primes_between(10, 30)
print(prime_numbers)
# print(f"Prime numbers between {start} and {end}: {prime_numbers}")
