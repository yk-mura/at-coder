A, B, C = map(int, input().split())

if C == 1:
    B -= 1

ans = 'Aoki' if A <= B else 'Takahashi'

print(ans)
