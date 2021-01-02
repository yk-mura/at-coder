N = int(input())

S = {}
for _ in range(N):
    s = input()

    if s[0] != '!':
        key = s
        bit = 0b01
    else:
        key = s[1:]
        bit = 0b10

    if key in S:
        S[key] |= bit

        if S[key] == 0b11:
            print(key)
            exit(0)
    else:
        S[key] = bit

print('satisfiable')
