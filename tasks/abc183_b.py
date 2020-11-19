sx, sy, gx, gy = map(float, input().split())

ans = (sx * gy + gx * sy) / (sy + gy)

print(ans)
