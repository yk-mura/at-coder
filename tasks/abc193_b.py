N = int(input())

ans = -1
for _ in range(N):
    A, P, X = map(int, input().split())
    if X > A and (ans == -1 or P < ans):
        ans = P

print(ans)
