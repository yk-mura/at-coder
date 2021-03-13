N = int(input())

ans = 0
for i in range(0, 6):
    d = 10 ** (i * 3)
    if N < d:
        break

    nd = 10 ** ((i+1) * 3)
    rangeA = d
    rangeB = min(nd-1, N)
    num = rangeB - rangeA + 1

    ans += num * i

print(ans)
