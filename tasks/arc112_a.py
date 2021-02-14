T = int(input())
for _ in range(T):
    L, R = map(int, input().split())

    if L == 0 and R == 0:
        print(1)
        continue
    if L == R:
        print(0)
        continue
        
    x = R - L

    if x < L:
        print(0)
        continue

    y = x - L + 1
    ans = int(y * (y+1) / 2)
    print(ans)
