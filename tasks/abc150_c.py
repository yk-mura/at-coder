import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = list(itertools.permutations(range(1, N + 1)))

a = l.index(P)
b = l.index(Q)
ans = abs(b - a)

print(ans)
