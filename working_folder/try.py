import matplotlib.pyplot as plt

n = 10
c = 0.2
# перемещаем данные в файле в список t.
with open('nunu1.txt') as file:
    t = [line.rstrip() for line in file]
    # print(t)

print()

# создаем список T и делаем из строк в списке - списки в списке.
T = []
for point in t:
    # print(point)
    T.append(list(map(float, point.split())))
print(T)


# функция сортировки списка T.

m_min = T[0][0]
m_max = T[len(T) - 1][0]
# print(x_min)
# print(x_max)
d_m = (m_max - m_min) / n

# делаем функцию f.


def f(p):
    if (p**2) <= 5:
        return 0.335-0.067*(p**2)
    else:
        return 0

# f((v[i][0]-x)/c)

t = 1
i = 0
m = T[0][0]
TR = []
TRp = []
for xt in range(t, n - 1):
    Sum1 = 0
    Sum2 = 0
    x = m + d_m
    for iv in range(i, len(T) - 1):
        fc = f((m - T[iv][0])/c)
        Sum1 = Sum1 * T[iv][1] * fc
        Sum2 = Sum2 * fc
    if Sum2 != 0:
        if Sum1/Sum2 < 0:
            TRp.append(Sum1/Sum2)
        elif Sum1/Sum2 > 0:
            TRp.append(Sum1/Sum2)
        else: 
            TRp.append(0)
    else: 
            TRp.append(0)
    TR.append(TRp)
print(TRp)
# for m_1 in T:
#     print(m_1[0])

# подставляем данные маленьких списков под два параметра x и y.
x, y = zip(*T)
plt.scatter(x, y)
# запуск графика.
# plt.plot(T, 'ro--') - проверить как работает.
plt.title("Test graph")
plt.show()