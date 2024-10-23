numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Список чисел:", numbers)
primes = []
not_primes = []
is_prime = True
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
        is_prime = True
print("Простые числа:", primes)
print("Составные числа: ", not_primes)

