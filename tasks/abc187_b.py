N = int(input())

points = []
for _ in range(N):
  X, Y = map(int, input().split())
  points.append((X, Y))

points.sort(key=lambda x: x[0])

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
        if a >= -1 and a <= 1:
            ans += 1

print(ans)