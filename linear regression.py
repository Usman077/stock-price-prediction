import numpy as np
import matplotlib.pyplot as plt
def estimate_coef(x, y):
    def estimate_coef(x, y):
        #number of observation/points
        n = np.size(x)
        # mean of x and y vector
        m_x = np.mean(x)
        m_y = np.mean(y)
def plot_regression_line(x,y,b):
    #plotting the actual points as scatter plot
    plt.scatter(x,y, color = "m", marker = "0", s = 30)
    #predict response vector
    y_pred = b[0] + b[1]*x
    #plotting the regression line
    plt.plot(x,y_pred, color = "g")
    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    # function to show plot
    plt.show()      