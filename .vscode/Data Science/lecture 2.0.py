import numpy as np
players = [14, 18, 19, 24, 26, 33, 42, 55, 67]
pl=np.array(players)
#mean
print("Mean = {0:.1f} ".format(np.mean(pl)))
#median
print("Median = {0:.1f} ".format(np.median(pl)))
#variance
print("Variance = {0:.1f} ".format(np.var(pl)))
#deviation
print("Standard deviation = {0:.1f} ".format(np.std(pl)))
stdv=np.std(pl)
print((pl[(pl>(pl-stdv) & pl>(pl+stdv))]))