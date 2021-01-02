N, M = map(str, input().split())

n = int(N[0]) + int(N[1]) + int(N[2])
m = int(M[0]) + int(M[1]) + int(M[2])
ans = max(n, m)

print(ans)