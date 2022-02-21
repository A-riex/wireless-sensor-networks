import scipy.io as sp
import numpy.matlib
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')   # plot style

P = 10
N = 1000
mean_axis = 0

for sigma_sq in range (10, 0, -1):

    # generate random values for H matrix
    H = np.random.rand(N,P)
    print("Observation matrix H is: ")
    print(np.shape(H))


    # generate random values for theta as a column vector
    theta = np.random.rand(P, 1)
    print("Parameter theta of dim P is: ")
    print(np.shape(theta))


    # Generate gaussian noise. w should probably be a NxP
    w = np.random.normal(0, sigma_sq, (N,P))
    print("w is the observation noise :")
    print(np.shape(w))


    x = np.dot(H, theta) + w
    print("x is :")
    print(np.shape(x))

    # theta = ((H^T .* H)^(-1)) .* (H^T .* x)
    theta_hat = np.dot(np.linalg.inv(np.dot(np.matlib.transpose(H),H)), np.dot(np.matlib.transpose(H),x))
    print("Theta hat is: ")
    print(np.shape(theta_hat))

    # Theta_theoretical = sigma_sq * (H^T .* H)^(-1)
    theta_theoretical = sigma_sq * np.linalg.inv( np.dot( np.matlib.transpose(H), H ) )
    print("theta theoretical is: ")
    print(np.shape(theta_theoretical))

    # calculate mean square error
    MSE_est = ((theta_hat - theta)**2).mean(axis=mean_axis)       
    print("MSE_est is: ")
    print(np.shape(MSE_est))

    # We should use trace aswell
    MSE_theo = ((theta_theoretical - theta)**2).mean(axis=mean_axis)
    print("MSE_theo is: ")
    print(np.shape(MSE_theo))

    # plot
    fig, ax = plt.subplots(figsize=(12, 4))
    plt.subplots_adjust(left = 0.038, bottom = 0.045)

    y = np.linspace(0, P, P)

    ax.plot(y, MSE_est, 'b', linewidth=2.0)
    ax.plot(y, MSE_theo, 'g', linewidth=2.0)

plt.show()
