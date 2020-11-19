WORDS = ['dream', 'dreamer', 'erase', 'eraser']

S = input()

ans = None
s = S
while True:
    isMatch = False
    for word in WORDS:
        if s.endswith(word):
            isMatch = True
            s = s[:-len(word)]
            break

    if not isMatch:
        ans = 'NO'
        break
    elif len(s) == 0:
        ans = 'YES'
        break

print(ans)
