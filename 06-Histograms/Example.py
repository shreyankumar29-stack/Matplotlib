from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

ages=[18, 19, 21, 25,26,26,30,32,38,45, 55]

# passing bins as a list
bins=[10,20,30,40,50,60]

plt.hist(ages, bins=bins,edgecolor='black')
plt.title('Ages of Respondents')
plt.xlabel('Age')
plt.ylabel('Number of Respondents')
plt.show()