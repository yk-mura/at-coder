r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r3, c3 = r2 - r1, c2 - c1

dist = abs(r3) + abs(c3)
ans = None
if r1 == r2 and c1 == c2:
    ans = 0
elif (r3 == c3 or r3 == -c3) or (dist <= 3):
    ans = 1
elif ((r3 ^ c3 ^ 1) & 1) or (dist <= 6) or (abs(r3 + c3) <= 3 or abs(r3 - c3) <= 3):
    ans = 2
else:
    ans = 3

print(ans)
