from matplotlib import pyplot as plt
import numpy as np
import openpyxl

# x = [2, 3, 4, 5, 6]
# y = [20, 30, 40, 50, 10]

# plt.bar(x,y)
# plt.scatter(x,y)
# plt.plot(x,y)
# plt.barh(x,y)

# plt.plot([1, 2, 3, 4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "y--")
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "bo")
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "gs")

# data = np.arange(0., 5., 0.2)
# print(data)

# plt.plot(data, data, "r--")
# plt.plot(data, data, "r--", data, data**2, "bo")
# plt.plot(data, data, "r--", data, data**2, "bo", data, data**3, "ys")

# data = {
#     'a': np.arange(50),
#     'c': np.random.randint(0, 50, 50),
#     'd': np.random.randn(50)
# }

# # print(data)

# data['b'] = data['a']+10*np.random.randn(50)
# data['d'] = np.abs(data['d'])*100

# # print(data)
# plt.scatter('a', 'b', c='c', s='d', data=data)

# -----------------------------------------------------------------
names = ['group_a', 'group_b', 'group_c']
values = [50, 20, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.savefig("myplot.png")

plt.show()

wb = openpyxl.load_workbook('input.xlsx')
ws = wb.active

img = openpyxl.drawing.image.Image('myplot.png')
ws.add_image(img, "A1")

wb.save('output.xlsx')