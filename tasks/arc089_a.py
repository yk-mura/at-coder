def getDistination(now_pos, next_pos):
    x = max(now_pos[0], next_pos[0]) - min(now_pos[0], next_pos[0])
    y = max(now_pos[1], next_pos[1]) - min(now_pos[1], next_pos[1])
    return x + y

N = int(input())
points = {}
for i in range(N):
    t, x, y = map(int, input().split())
    points[t] = (x, y)

ans = "Yes"
now_time = 0
now_pos = (0, 0)
for next_time in points.keys():
    next_pos = points[next_time]

    req_dist = getDistination(now_pos, next_pos)
    req_time = next_time - now_time

    rem_time = req_time - req_dist
    if rem_time >= 0 and rem_time % 2 == 0:
        now_time = next_time
        now_pos = next_pos
    else:
        ans = "No"
        break

print(ans)