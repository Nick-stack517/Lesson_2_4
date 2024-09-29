numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for k in range(len(numbers)):
    # print(numbers[k], ',k=', k) #####
    if numbers[k] > 1:
        # print('> 1') #

        # Iterate from 2 to n // 2
        for i in range(2, (numbers[k] // 2) + 1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (numbers[k] % i) == 0:
                # print(numbers[k], "# is not a prime number")
                not_primes.append(numbers[k])
                break
        else:
            # print(numbers[k], "# is a prime number")
            primes.append(numbers[k])


    # else:
        # print(numbers[k], '<1')
        # print(numbers[k], " 111111111 ")

print('Primes: ', primes)
print('Not Primes: ', not_primes)
