min_value = 1
max_value = 5000

#calculate prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# creates list of primes
primes = []
for x in range(min_value, max_value + 1):
    if is_prime(x):
        primes.append(x)

#retrieve factors
def prime_factorization(input, list_of_numbers):
    factors = {}
    temp_num = input
    for prime in list_of_numbers:
        if prime > temp_num:
            break
        power = 0
        while temp_num % prime == 0:
            temp_num //= prime
            power += 1

        if power > 0:
            factors[prime] = power
    return factors

while True:
    number = int(input(f"Enter a number ({min_value}-{max_value}): "))
    if min_value <= number <= max_value:
        break
    else:
        print(f"Please enter a number between {min_value} and {max_value}.")

#returns dict
prime_factors_with_powers = prime_factorization(input=number, list_of_numbers=primes)
factor_list = []

#formats powers
for prime, power in prime_factors_with_powers.items():
    if power == 1:
        factor_list.append(str(prime))
    else:
        factor_list.append(f"{prime}^{power}")

#prints in product format
print(f"{number} = ", end='')
print(" x ".join(factor_list))

