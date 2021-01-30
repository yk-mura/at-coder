aList = []
bList = []
cList = []
dList = []

N, M = map(int, input().split())
for _ in range(M):
    A, B = map(int, input().split())
    aList.append(A)
    bList.append(B)

K = int(input())
for _ in range(K):
    C, D = map(int, input().split())
    cList.append(C)
    dList.append(D)

patterns = list(set())
for i in range(2**K):
    pattern = set()
    for k in range(K):
        if 2**k & i:
            pattern.add(cList[k])
        else:
            pattern.add(dList[k])
    patterns.append(pattern)

max = 0
for pattern in patterns:
    match = 0
    for n in range(M):
        if aList[n] in pattern and bList[n] in pattern:
            match += 1

    if match > max:
        max = match

print(max)
