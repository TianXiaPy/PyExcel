import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [20, 40, 30, 50]
plt.barh(x, y,
         height=0.5,
         left=10,
         align="center",
         edgecolor="y",
         color="blue")
plt.show()
