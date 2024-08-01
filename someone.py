import matplotlib.pyplot as plt

Catigories = ['A','B','C','D','E']
Values = [7,12,5,18,10]

#Creating a horizontal bar graph
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.barh(Catigories,Values,color='b')
plt.title('Horizontal Bar Graph')
plt.xlabel('Value')
plt.ylabel('Catigories')
plt.show()