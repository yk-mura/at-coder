import sys
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

H, W = map(int, input().split())
a = {}
secs = {}
warps = {}
for i in range(H):
    l = input()
    for j in range(len(l)):
        c = l[j]

        p = (i, j)
        a[p] = c

        if c == '#':
            secs[p] = -1
        elif c == 'S':
            S = p
            secs[p] = 0
        elif c == 'G':
            G = p
        elif c.islower():
            if c not in warps:
                warps[c] = [p]
            else:
                warps[c].append(p)

queue = deque()
queue.append(S)

while len(queue):
    p = queue.popleft()
    c = a[p]
    s = secs[p]
    ns = s + 1

    for dir in DIRS:
        np = (p[0] + dir[0], p[1] + dir[1])
        if np[0] < 0 or np[0] >= H or np[1] < 0 or np[1] >= W:
            continue

        nc = a[np]

        if np in secs:
            continue
        if nc == '#':
            continue
        if nc == 'G':
            print(ns)
            sys.exit(0)
        
        secs[np] = ns
        queue.append(np)

    if c.islower():
        for wp in [wp for wp in warps[c] if wp != p and wp not in secs]:
            secs[wp] = ns
            queue.append(wp)

print(-1)