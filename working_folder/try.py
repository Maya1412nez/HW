""" slovary = {1: 2}
i = 2
c = 0
evens = []
while c < 101:
    i += 1
    f = 0
    for num in evens:
        if i % num == 0:
            f = 1
    if f == 0:
        evens.append(i)
        slovary[i] = i * 2
        c += 1
for k, v in slovary.items():
    if not ('8' in str(k) or 8 in str(v)):
        del slovary[k] """

a = 'Из-за игры отменился проект. УРА'
b = 'Из-за важной игры отменился проект. УРА'
def up_game(a):
    return(a[:a.find('игры')] + a[a.find('игры'):a.find('отменился')].upper() + a[:a.find('отменился'):])
print(up_game(a))
print(up_game(b))