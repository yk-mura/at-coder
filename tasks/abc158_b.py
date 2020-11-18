N, A, B = map(int, input().split())

cnt = A + B
ans = A * int(N / cnt)
ans += min(int(N % cnt), A)

print(ans)
