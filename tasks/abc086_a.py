a, b = map(int, input().split())

c = a * b
ans = "Even" if c % 2 == 0 else "Odd"

print(ans)
