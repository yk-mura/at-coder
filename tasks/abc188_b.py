N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = 0
for i in range(N):
    x += a[i] * b[i]

ans = 'Yes' if x == 0 else 'No'

print(ans)
