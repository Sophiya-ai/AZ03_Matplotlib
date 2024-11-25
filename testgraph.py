import matplotlib.pyplot as plt

# x = [2,6,7,8,14,20]
# y = [5,10,7,9,10,16]
#
# plt.plot(x,y) #функция создания линейного графика
# plt.title("Test line graph")
# plt.xlabel('x')
# plt.ylabel('y')
#plt.show()

#гистограмма
# data = [5, 2, 7, 8, 4, 6, 3, 5, 7, 8, 5, 3, 9]
# plt.hist(data, bins=3)
# plt.title("Сколько спят люди")
# plt.xlabel('часы сна')
# plt.ylabel('количество людей')
# plt.show()

#диаграмма рассеивания
x = [1,4,6,7,6, 3, 5, 7, 8, 5, 3, 9]
y = [6, 3, 5, 7, 8, 5, 3, 9,5,10,3,8]
plt.scatter(x,y)
plt.title("Диаграмма рассеивания")
plt.xlabel('x')
plt.ylabel('y')
plt.show()