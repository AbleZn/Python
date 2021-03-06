# scatter_square
# Created by JKChang
# 22/01/2018, 13:35
# Tag:
# Description: 

import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x ** 3 for x in x_values]

plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=10)
plt.title('Cube', fontsize=20)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube value', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('resources/cube.png')
plt.show()
