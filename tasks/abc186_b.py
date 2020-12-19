H, W = map(int, input().split())

lines = []
minimum = None
for _ in range(H):
    line = list(map(int, input().split()))
    _min = min(line)
    if minimum == None or _min < minimum:
        minimum = _min

    lines.append(line)
    
ans = 0
for line in lines:
    for v in line:
        ans += (v - minimum) 

print(ans)