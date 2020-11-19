N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    digits = [int(x) for x in list(str(i))]
    dig_sum = sum(digits)
    if dig_sum >= A and dig_sum <= B:
        ans += i

print(ans)
