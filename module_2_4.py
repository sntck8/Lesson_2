numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Список чисел:", numbers)
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i > 1:
        for k in range(2, i):
            if (i % k) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
        is_prime = True
print("Простые числа:", primes)
print("Составные числа: ", not_primes)
