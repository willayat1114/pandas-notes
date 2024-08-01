import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a bar graph
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(range(1, 6), [data.count(i) for i in range(1, 6)], color='b')
plt.title('Bar Graph')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Create a histogram
plt.subplot(1, 2, 2)
plt.hist(data, bins=range(1, 7), edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the graphs
plt.tight_layout()
plt.show()