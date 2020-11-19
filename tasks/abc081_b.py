N = int(input())
A = list(map(int, input().split()))

ans = 0
isBreak = False
while True:
    for i in range(len(A)):
        if A[i] == 0:
            isBreak = True
            break
        elif A[i] % 2 == 0:
            A[i] /= 2
        else:
            isBreak = True
            break
    
    if isBreak:
        break

    ans += 1

print(ans)
