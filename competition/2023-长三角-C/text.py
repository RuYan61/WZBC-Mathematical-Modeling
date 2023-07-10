import numpy as np
import pandas as pd

def GM11(x0): # x0: original data, a list
    x1 = x0.cumsum() #1-AGO accumulation
    z1 = (x1[:len(x1)-1] + x1[1:])/2.0 #mean sequence
    z1 = z1.reshape((len(z1),1))
    B = np.append(-z1, np.ones_like(z1), axis = 1)
    Y = x0[1:].reshape((len(x0)-1, 1))
    [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y) #parameters estimation
    f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2)) #time response function
    delta = np.abs(x0 - np.array([f(i) for i in range(1,len(x0)+1)]))
    C = delta.std()/x0.std()
    P = 1.0*(np.abs(delta - delta.mean()) < 0.6745*x0.std()).sum()/len(x0)
    return f, a, b, x0[0], C, P #model function, a, b, x0[0], C, P

# Sample usage
data = np.array([34.60, 33.33, 35.93, 32.02, 27.97, 29.04, 27.87, 24.15])
f,a,b,x0,C,P = GM11(data)
print(f(20)) # Prediction for t = 5
