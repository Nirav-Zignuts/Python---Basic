def prime_sum(n):
    prime = []
    start = 2
    while len(prime) < n:
        for i in range(2, start):
            if start % i == 0:
                break
        else:
            prime.append(start)
        start += 1
    print(prime)
    return sum(prime)

count = int(input("how many first N prime numbers sum you want: "))
print(prime_sum(count))
