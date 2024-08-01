import matplotlib.pyplot as plt 
# Data for the histogram
data = [1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# Plotting the histogram
plt.hist(data, bins=5)
# Adding a title
plt.title('Histogram')
# Displaying the chart
plt.show()
