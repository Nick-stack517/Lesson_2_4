numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for k in range(len(numbers)):
    is_prime = True
    if numbers[k] > 1:
        for i in range(2, (numbers[k] // 2) + 1):
            if (numbers[k] % i) == 0:
                is_prime = False
                break
        else:
            is_prime = True
        if is_prime == True:
            primes.append(numbers[k])
        else:
            not_primes.append(numbers[k])
print('Primes: ', primes)
print('Not Primes: ', not_primes)
