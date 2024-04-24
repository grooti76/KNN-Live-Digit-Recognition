import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


class DIGIT_CLASSIFIER:
    def __init__(self,training_data:str) -> None:
        self.training_data = training_data
    
    def process_data(self):
        train_df = pd.read_csv(self.training_data)
        train_x = train_df.drop('label',axis=1)
        train_y = train_df['label']
        return train_x,train_y
    
    def train(self,x_train,y_train,num_neighbors=3):
        self.model = KNeighborsClassifier(n_neighbors=num_neighbors)
        self.model.fit(x_train,y_train)
        
    def predict(self,x_test):
        return self.model.predict(x_test)
    
    def decoder(self,x):
        return np.argmax(x,axis=1)
    
    def process_test_data(self,test_data:str):
        test_df = pd.read_csv(test_data)
        return test_df

    