def calc(x):
    xStr = str(x)

    xDesc = sorted(xStr, reverse=True)
    g1 = int(''.join(xDesc))

    xAsc = sorted(xStr)
    g2 = int(''.join(xAsc))

    f = g1 - g2
    return f

N, K = map(int, input().split())

x = N
for _ in range(K):
    x = calc(x)

print(x)
