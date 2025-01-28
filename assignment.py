import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,]) # x axis
y = np.array([2,4,6,8,10])# y axis

n = len(x)

# get the values needed 
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

m = ( n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2) # using the formula
b = (sum_y - m * sum_x) / n

print(f"Linear regression equation: y = {m:.2f}x + {b:.2f}")

plt.scatter( x, y, color="blue", label=" Data Points")

y_pred = m * x + b
plt.plot(x, y_pred, color="red", label="regression line") 

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear regression")
plt.legend

plt.show()