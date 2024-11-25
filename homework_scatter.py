import numpy as np
import matplotlib.pyplot as plt

#диаграмма рассеивания
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x,y)
plt.title("Диаграмма рассеивания")
plt.xlabel('x')
plt.ylabel('y')
plt.show()