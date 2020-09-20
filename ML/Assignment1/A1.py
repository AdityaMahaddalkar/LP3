import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


class LinearRegression(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.dataset = None
        self.X = None
        self.Y = None
        self.b_0 = random.randint(1, 20)
        self.b_1 = random.randint(1, 20)

    def read_dataset(self):
        self.dataset = pd.read_csv(self.file_name)

        self.X = self.dataset.iloc[:, 0]
        self.Y = self.dataset.iloc[:, -1]

    def calculate_coefficient(self, max_epochs=100000, alpha=0.001):

        y_pred = self.b_0 * self.X + self.b_1
        n = self.X.shape[0]
        for epochs in range(max_epochs):

            loss = (1 / 2 * n) * np.sum((self.Y - y_pred) ** 2)
            self.b_0 -= alpha * (2 / n) *\
                np.sum(np.dot(self.Y - y_pred, self.X))
            self.b_1 -= alpha * (2 / n) * np.sum(self.Y - y_pred)
            y_pred = self.b_0 * self.X + self.b_1

            if epochs % 1000 == 0:
                print(f"Epoch : {epochs} | Loss : {loss}")

    def Regression(self, max_epochs=100000, alpha=0.001):
        self.calculate_coefficient(max_epochs, alpha)
        print("Equation of line : Y = {} + {}*X".format(self.b_0, self.b_1))

    def plot_line(self):
        plt.scatter(self.X, self.Y, color="m", marker="o", s=30)

        # predicted response vector
        y_pred = self.b_0 + self.b_1*self.X

        # plotting the regression line
        plt.plot(self.X, y_pred, color="g")

        # putting labels
        plt.xlabel('x')
        plt.ylabel('y')

        # function to show plot
        plt.show()


if __name__ == '__main__':
    regressor = LinearRegression('data/sample.csv')
    regressor.read_dataset()
    regressor.Regression(10000, 0.00000001)
    regressor.plot_line()
