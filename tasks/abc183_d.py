import itertools

N, W = map(int, input().split())
use = [0] * 200001
for n in range(N):
    S, T, P = map(int, input().split())
    use[S] += P
    use[T] -= P

failed = False
using = 0
for u in use:
    using += u
    if using > W:
        failed = True
        break

print('Yes' if not failed else 'No')
