from collections import Counter

N, K = map(int, input().split())
a = list(map(int, input().split()))

m = max(a)
numbers = Counter(a)
for i in range(1, m+1):
    if i not in numbers:
        numbers[i] = 0

box = K
ans = 0
for i in range(m+1):
    box = min(box, numbers[i])
    ans += box

print(ans)
