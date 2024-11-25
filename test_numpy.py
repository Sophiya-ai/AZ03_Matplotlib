import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,6,4])
print(a)

b = np.zeros((3,5))
print(b)

c = np.ones((3,5))
print(c)

d = np.random.random((3,5))
print(d)

#массив от 0 до 10 с шаком 2
d1 = np.arange(0,10,2)
print(d1)

#массив равнораспределнных чисел
d2 = np.linspace(0,1,10)
print(d2)

#строим график
x = np.linspace(-10,10,100)
y = x**2
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Грфик функции y=x**2')
plt.grid(True) # делаем сетку графика
plt.show()