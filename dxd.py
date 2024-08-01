import matplotlib.pyplot as plt

# List of x-coordinates
x = [1, 2, 3, 4, 5]

# List of y-coordinates
y = [2, 4, 1, 3, 5]

# Create a line plot
plt.plot(x, y)

# Set the labels for the x and y axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the graph
plt.title('My Graph')

# Display the graph
plt.show()