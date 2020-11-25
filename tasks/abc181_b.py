N = int(input())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    aSum = a * (a - 1) // 2
    bSum = b * (b + 1) // 2
    ans += bSum - aSum

print(ans)