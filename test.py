import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_axes(rect=(10, 10, 10, 10), label='label', projection='polar')
ax2 = fig.add_axes(rect=(5, 10, 5, 10), frameon=False, facecolor='g')

ax1.plot([0, 1, 2], [2, 5, 6])
ax2.plot([0, 1, 6], [2, 5, 10])

fig.show()
plt.show()
