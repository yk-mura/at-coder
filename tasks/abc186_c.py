N = int(input())

ans = 0
for i in range(1, N+1):
    base10 = str(i)
    base8 = oct(i)
    if '7' not in base10 and '7' not in base8:
        ans += 1

print(ans)