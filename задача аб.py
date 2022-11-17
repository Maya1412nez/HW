filik = open('ЗадачаАБ.txt', 'r')
minn, maxx = 10000000, -10000000

listik = []

for row in filik:
    listik.append(int(row))
    if int(row) < minn:
        minn = int(row)
    if int(row) > maxx:
        maxx = int(row)
control_sum = maxx + minn
print(listik)
print(max(listik), min(listik))
""" print(control_sum)
 """
""" for row in filik:
    
 """