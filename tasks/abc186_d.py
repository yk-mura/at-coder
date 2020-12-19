N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
s = 0
for i in range(1, N):
    
    x = A[i] * i
    s += A[i-1]
    ans += x - s

print(ans)
