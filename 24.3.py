
file = open("24.txt")
s = file.read()
m = 1
k = 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        k = k + 1
    else:
        k = 1
    print(m)