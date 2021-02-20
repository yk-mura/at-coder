S = input()

ans = 'Yes'
for i in range(len(S)):
    if not ((i % 2 and S[i].isupper()) or (i % 2 == 0 and S[i].islower())):
        ans = 'No'
        break

print(ans)
