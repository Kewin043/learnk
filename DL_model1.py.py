import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

observation = 1000
xs = np.random.uniform(-10,10,(observation,1))
zs = np.random.uniform(-10,10,(observation,1))
input = np.column_stack((xs,zs))
print(input.shape)

noise = np.random.uniform(-1,1,(observation,1))
targets = 13*xs+7*zs - 12 + noise
print(targets.shape)

tragets = targets.reshape(observation,)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs,zs,targets)
ax.set_xlabel('xs')
ax.set_ylabel('zs')
ax.set_zlabel('Targets')
ax.view_init(azim = 100)
plt.show()
tragets = tragets.reshape(observation ,1)

init_range = 0.1
weights = np.random.uniform(-init_range,init_range,size=(2,1))
biases = np.random.uniform(-init_range,init_range,size=1)
print(weights)
print(biases)

learning_rate= 0.02

for i in range(100):
    outputs = np.dot(input,weights) + biases
    deltas = outputs - targets

    loss = np.sum(deltas**2)/2/observation
    print(loss)
    deltas_scaled = deltas/observation
    weights = weights - learning_rate*np.dot(input.T,deltas_scaled)
    biases = biases - learning_rate*np.sum(deltas_scaled)
    print(weights,biases)
    plt.plot(outputs,tragets)
    plt.xlabel('outputs')
    plt.ylabel('targets')
    plt.show
