_ = input()
s = input()

s2 = ''
for c in s:
    s2 += c
    if s2[-3:] == 'fox':
        s2 = s2[:-3]

print(len(s2))
