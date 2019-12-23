import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LinearRegression(object):
    def __init__(self,file_name):
        self.file_name=file_name
        self.dataset=None
        self.X=None
        self.Y=None
        self.b_0=0
        self.b_1=0
        
 
    def read_dataset(self):
        self.dataset=pd.read_csv(self.file_name)

        self.X=self.dataset.iloc[:,0]
        self.Y=self.dataset.iloc[:,-1]
        
    def calculate_coefficient(self):
        n=np.size(self.X)
        
        mean_x=np.mean(self.X)
        mean_y=np.mean(self.Y)
        
        #calculate cross deviation and deviation about x
        
        xy=np.sum(self.Y*self.X)-n*mean_y*mean_x
        xx=np.sum(self.X*self.X)-n*mean_x*mean_x
        
        #coefficients
        self.b_1=xy/xx
        self.b_0=mean_y-self.b_1*mean_x
        
        
        
    def Regression(self):
        self.calculate_coefficient()
        print("Equation of line : Y = {} + {}*X".format(self.b_0,self.b_1))
        
    def plot_line(self):
        plt.scatter(self.X, self.Y, color = "m", marker = "o", s = 30) 
  
        # predicted response vector 
        y_pred = self.b_0 + self.b_1*self.X 

        # plotting the regression line 
        plt.plot(self.X, y_pred, color = "g") 

        # putting labels 
        plt.xlabel('x') 
        plt.ylabel('y') 

        # function to show plot 
        plt.show()
    
if __name__=='__main__':
    regressor=LinearRegression('data/sample.csv')
    regressor.read_dataset()
    regressor.Regression()
    regressor.plot_line()

