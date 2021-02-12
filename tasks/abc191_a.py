V, T, S, D = map(int, input().split())

a = V * T
b = V * S

ans = 'No' if a <= D and D <= b else 'Yes'

print(ans)
