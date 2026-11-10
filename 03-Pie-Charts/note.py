from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0, 0, 0, 0.1, 0] # only "explode" the 4th slice (i.e. 'Python')
plt.pie(slices,
        labels=labels,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90,
        wedgeprops={'edgecolor':'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()