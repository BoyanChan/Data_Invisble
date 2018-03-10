import matplotlib.pyplot as plt
from RandomWalk.random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.num_point)),
            cmap=plt.cm.Greens, edgecolors='none', s=1)


plt.scatter(0, 0, c='Blue', edgecolors='none', s=10)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.figure(dpi=500,figsize=(10,6))

# 1.x的值,s=10)
plt.show()
