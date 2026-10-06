import matplotlib.pyplot as plt
import numpy as np

# # Basic Line Plot
# x = np.array([1, 2, 3, 4])
# y = np.array([10, 20, 25, 30])
# plt.plot(x, y)
# plt.title("Basic Line Plot")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# plt.show()

# # Styled Line Plot
# x = np.array([1, 2, 3, 4])
# y = np.array([3, 8, 1, 10])
# plt.plot(y, linestyle='dotted', color='green', marker='o')
# plt.title('Styled Line Example')
# plt.show()

# # Multiple Line Plot
# x = np.array([1, 2, 3, 4])
# y1 = np.array([2, 4, 6, 8])
# y2 = np.array([1, 3, 5, 7])
# plt.plot(x, y1, label='Line 1', color='red', marker='s')
# plt.plot(x, y2, label='Line 2', color='blue', linestyle='--', marker='o')
# plt.title('Multiple Line Example')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.legend()
# plt.show()

# BarChart with Numpy and Matplotlib

# x = np.array(["Salary", "Expense", "Charity", "Food", "Travel"])
# y = np.array([5, 9, 1, 4, 7])

# plt.bar(x, y, color='orange')
# plt.title("Bar Chart Example")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

# Scatter Plot with Numpy and Matplotlib
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 4, 3, 6, 7])
# plt.scatter(x, y, color='purple', s=100)
# plt.title('Scatter Plot Example')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.show()

# Histogramm

# data = np.array([3, 4, 5, 6, 7, 8, 8, 6, 9, 10])

# plt.hist(data, bins=5, color='skyblue', edgecolor='black')
# plt.title('Histogramm Example')
# plt.xlabel('Values')
# plt.ylabel('Counts')
# plt.show()

# Subplots -> Multiple Graphs Togather

# x = np.array([1, 2, 3, 4])
# y1 = np.array([2, 4, 6, 8])
# y2 = np.array([3, 6, 9, 12])

# plt.figure(figsize=(8, 4))  # width , height

# plt.subplot(1, 2, 1)
# plt.plot(x, y1, color='red')
# plt.title("Plot 1")

# plt.subplot(1, 2, 2)
# plt.bar(x, y2, color='blue')
# plt.title("Plot 2")

# plt.tight_layout()
# plt.savefig('my_plot.png')  # saves in current folder
# plt.show()

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap="Blues")

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
