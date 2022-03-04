import numpy as np
import matplotlib.pyplot as plt
import numpy.random as randgen

d = {"Name" : "Alexander Riex", "Age": 24, "Shoesize": 37}
print(d)
print(d["Age"])
print(d.values())
print(d.keys())
d["Height"] = 1.97
print(d)
del(d["Shoesize"])
print(d)

var = [0, 1, 2, 3, 4, 5]
print(var[0:3])


# Logic tutorial
A = 1
B = 2

print(A==B)
print(A!=B)

# if statements
if (A!=B):
    print("A!=B")
else:
    print("if statement false")


for i in range(0, 7, 3):
    print(i)


A = 5
B = .1
N = 100
mu = 0
sigma = 1
w = randgen.normal(mu, sigma)
seq = np.arange(0, N, 1, dtype=int)
x = A + B*seq + w




