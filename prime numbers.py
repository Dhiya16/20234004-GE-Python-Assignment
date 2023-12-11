
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_up_to_n(n):
    """Generate all prime numbers up to n."""
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes

def generate_first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


n = int(input("Enter a number (n): "))


if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

primes_up_to_n = generate_primes_up_to_n(n)
print(f"Prime numbers up to {n}: {primes_up_to_n}")


first_n_primes = generate_first_n_primes(n)
print(f"First {n} prime numbers: {first_n_primes}")
