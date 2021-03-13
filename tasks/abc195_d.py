class Item:
    size = 0
    value = 0

    def __init__(self, s, v):
        self.size = s
        self.value = v

class Box:
    size = 0
    value = 0

    def __init__(self, s, v):
        self.size = s
        self.value = v

N, M, Q = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append(Item(W, V))
items.sort(key=lambda item: item.value, reverse=True)

boxSizes = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1

    boxes = []
    for i in range(len(boxSizes)):
        if i >= L and i <= R:
            continue

        boxes.append(Box(boxSizes[i], 0))

    boxes.sort(key=lambda box: box.size)
    for item in items:
        for box in boxes:
            if box.value != 0:
                continue

            if item.size <= box.size:
                box.value = item.value
                break

    ans = 0
    for box in boxes:
        ans += box.value
    print(ans)
