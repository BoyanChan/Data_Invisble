import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Greens,edgecolors='none',s=10)
#1.x的值
#2.y的值
#3.4.将y值转成渐变色,值越大,颜色越深
#5.去除点的轮廓
#6.设定每个点的大小
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis([0,1000,0,1000000])#控制坐标轴的取值范围
plt.savefig('square.png',bbox_inches='tight')#用于将文件保存到文件目录下
plt.show()
