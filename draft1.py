slovary = {1: 2}
i = 2
evens = []
while i < 101:
    i += 1
    f = 0
    for num in evens:
        if i % num == 0:
            f = 1
    if f == 0:
        evens.append(i)
        slovary[i] = i * 2
for k, v in slovary.items():
    print(k, v)