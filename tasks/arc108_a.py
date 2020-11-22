S, P = map(int, input().split())
min = min(S, P)

ans = 'No'
for i in range(1, min):
    if i * (S - i) == P:
        ans = 'Yes'
        break

print(ans)
