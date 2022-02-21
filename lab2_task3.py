import scipy.io as sp
import numpy.matlib
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')   # plot style

P = 10
N = 1000
mean_axis = 0
sigma_sq = 1
i = 0
vector_MSE_est = np.zeros(10)
vector_MSE_theo = np.zeros(10)

while (sigma_sq <= 10):

    # generate random values for H matrix
    H = np.random.rand(N,P)
    print("Observation matrix H is: ")
    print(np.shape(H))

    I_w = sigma_sq * np.matlib.eye(N)
    print("I_w matrix is ")
    print(np.shape(I_w))

    I_th = sigma_sq * np.matlib.eye(P)
    print("I_w matrix is ")
    print(np.shape(I_w))

    # generate random values for theta as a column vector
    theta = np.random.normal(0,sigma_sq, (P,1))
    print("theta of dim P is: ")
    print(np.shape(theta))


    # Generate gaussian noise. w should probably be a NxP
    w = np.random.normal(0, sigma_sq,(N,1))
    print("w is :")
    print(np.shape(w))


    x = np.dot(H, theta) + w
    print("x is :")
    print(np.shape(x))

    # theta = 
    theta_hat =  np.dot((1/sigma_sq) * np.linalg.inv((1/sigma_sq) * I_th  + (1/sigma_sq) * np.dot(np.matlib.transpose(H),H)),np.dot(np.matlib.transpose(H),x))
    # theta_hat = theta_hat.mean()
    print("Theta hat is: ")
    print(np.shape(theta_hat))

    # Theta_theoretical = 
    MSE_theo = np.trace(np.linalg.inv((1/sigma_sq) * I_th  +  (1/sigma_sq)* (np.dot(np.matlib.transpose(H), H))))
    print("MSE_theo is: ")
    print(np.shape(MSE_theo))

    # calculate mean square error
    MSE_est = (np.square(theta_hat - theta)).mean()       
    print("MSE_est is: ")
    print(np.shape(MSE_est))

    vector_MSE_est[i] = MSE_est
    vector_MSE_theo[i] = MSE_theo
    i+=1
    sigma_sq+=1


print("mse_est_vector:")
print(vector_MSE_est)
print("mse_theo_vector:")
print(vector_MSE_theo)

# plot
fig, ax = plt.subplots(figsize=(12, 4))
plt.subplots_adjust(left = 0.038, bottom = 0.045)

y = np.linspace(0, 10, 10)

ax.plot(y, vector_MSE_est, 'b', linewidth=2.0)
ax.plot(y, vector_MSE_theo, 'g', linewidth=2.0)

plt.show()
