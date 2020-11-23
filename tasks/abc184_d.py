A, B, C = map(int, input().split())

results = {}

def calc(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0

    key = (a, b, c)
    if key in results:
        return results[key]

    total = a + b + c
    result = 0
    if a > 0:
        result += (calc(a + 1, b, c) + 1) * a / total
    if b > 0:
        result += (calc(a, b + 1, c) + 1) * b / total
    if c > 0:
        result += (calc(a, b, c + 1) + 1) * c / total

    results[key] = result
    return result

ans = calc(A, B, C)

print(ans)
