import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [4, 7, 2, 9]

# رسم نمودار ستونی
plt.bar(categories, values)

# نمایش نمودار
plt.savefig("myplot.png")
plt.show()