# Final Project for CS 244 - Dino Data Analysis using clusters

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("Loading Dino Data...")


DATA = np.loadtxt("clusterReady_cleanCompleteNoDates.csv", delimiter=',', skiprows=1)
print("Shape Data: ", DATA.shape)
