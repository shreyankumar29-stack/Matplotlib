from matplotlib import colors, pyplot as plt

plt.style.use("fivethirtyeight")

minutes=[1,2,3,4,5,6,7,8,9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]


labels=['player 1', 'player 2', 'player 3']
colors=[ '#6d904f','#fc4f30','#008fd5']
plt.stackplot(minutes, player1, player2, player3,labels=labels,colors=colors)

## What does that tuple mean? It is the location of the legend. The first number is the x coordinate and the second number is the y coordinate. The coordinates are in axes fraction, meaning that (0,0) is the bottom left of the axes and (1,1) is the top right of the axes. So (0.07,0.05) means that the legend will be placed 7% from the left and 5% from the bottom of the axes.
plt.legend(loc=(0.07,0.05))
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
