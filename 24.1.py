file = open('24.txt','r')
file_content = file.read()
l = file_content.split('\n')
dlinastr = 0
max = 10 ** 9
for i in range(len(s)):
    k = s[i].count("G")  # Считаем кол-во G в i-той строке
    if k < max:
        max = k
        dlinastr = i
# Ищем самую частую букву
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = ''
numb_a = 0
for i in alp:
    k = s[dlinastr].count(i)
    if numb_a <= k:
        numb_a = k
        a = i

print(a)