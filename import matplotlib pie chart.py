import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Label 1', 'Label 2', 'Label 3','Label 4','Label 5']
sizes = [20, 20, 20, 20, 200]  # Values should add up to 100

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Adding a title
plt.title('Pie Chart')

# Displaying the chart
plt.show()