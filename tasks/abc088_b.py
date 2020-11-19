N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = sum(a[::2])
bob = sum(a[1::2])
ans = alice - bob

print(ans)
