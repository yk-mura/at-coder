N, X = map(int, input().split())
s = input()

ans = X
for i in s:
    if i == 'x':
        ans -= 1
        if ans <= 0:
            ans = 0
    else:
        ans += 1

print(ans)
