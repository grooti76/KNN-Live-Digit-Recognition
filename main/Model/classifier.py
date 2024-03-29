import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier


class KNN_DIGIT_CLASSIFIER:
    def __init__(self,params:list) -> None:
        self.train_dataset = params[0]
        self.test_dataset = params[1]
        if len(params) > 2:
            raise Exception("Invalid number of arguments")
        pass
    
    def process(self):
        train_data = pd.read_csv(self.train_dataset)
        test_data = pd.read_csv(self.test_dataset)
        X = train_data.drop('label', axis=1)
        y = train_data['label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        
        return X_train, X_test, y_train, y_test, test_data
    
    
    def train(self, X_train, y_train,num_neighbors:int=3):
        knn = KNeighborsClassifier(n_neighbors=num_neighbors)
        knn.fit(X_train, y_train)
        return knn
        
    def predict(self, model, X_test):
        return model.predict(X_test)
    
    def evaluate(self, y_test, y_pred):
        acc = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        cr = classification_report(y_test, y_pred)
        return acc, cm, cr