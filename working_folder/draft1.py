# print(sum(map(int, list((str(int(input())))))))

# class Number:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.sum_val = (sum(map(int, list((str(int(val)))))))


# def to_d(x):
#     d = {}
#     for el in x:
#         d[(sum(map(int, list((str(int(el)))))))] = str(el)
#     return d

# x = [11, 10, 14, 3]

# dictik = to_d(x)
# for i in range(len(dictik)):
#     print(dictik[sorted(dictik)[i]])
    
y = [11, 3, 14, 41]
z = [112, 32, 142, 102]

def to_d1(y, z):
    y1 = sorted(y)
    d = {}
    for i in range(z):
        d[z[i]] = [y1.index[y[i]] ] # значение связанного списка, индекс должного 
    return d

d = to_d1(y, z)
s = sorted(d.values())
for el in s:
    print(d[el])


    