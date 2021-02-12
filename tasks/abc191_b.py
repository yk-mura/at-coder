N, X = map(int, input().split())
A = list(map(int, input().split()))

A = [a for a in A if a != X]
ans = ' '.join(map(str, A))

print(ans)
