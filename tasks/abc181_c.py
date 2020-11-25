N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x1, y1 = points[i]

    for j in range(i):
        x2, y2 = points[j]
        x2 -= x1
        y2 -= y1

        for k in range(j):
            x3, y3 = points[k]
            x3 -= x1
            y3 -= y1

            if x2 * y3 == x3 * y2:
                print("Yes")
                exit()

print('No')