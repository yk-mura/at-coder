N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

aMax = 0
m = 0
for n in range(N):
    if aMax < a[n]:
        aMax = a[n]

    tm = aMax * b[n]
    m = max(m, tm)

    print(m)
