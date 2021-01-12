N = int(input())
rates = list(map(int, input().split()))

playerIds = range(1, 2**N+1)

while len(playerIds) > 2:
    nextPlayerIds = []
    for j in range(0, len(playerIds), 2):
        aId = playerIds[j]
        bId = playerIds[j+1]
        aRate = rates[aId-1]
        bRate = rates[bId-1]

        winnerId = aId if aRate > bRate else bId
        nextPlayerIds.append(winnerId)

    playerIds = nextPlayerIds


aId = playerIds[0]
bId = playerIds[1]
aRate = rates[aId-1]
bRate = rates[bId-1]
loserId = aId if aRate < bRate else bId
print(loserId)
