N = int(input())
lim = 10 ** 5

numbers = set()
for i in range(2, lim):
    for j in range(2, lim):
        n = i ** j
        if n > N:
            break

        numbers.add(n)

print(N - len(numbers))
