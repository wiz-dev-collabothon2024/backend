import pandas as pd
import joblib
import numpy as np
from sklearn import tree
import os

class RandomForestClassifier():
    def __init__(self,
                 n_estimators: int =100,
                 max_depth: int =None,
                 random_state: int =1
                 ):
        print(f"Current directory: {os.getcwd()}")
        self.clf = joblib.load("./ml_model/random_forest_classifier_interpretable_152.joblib")
        self.data = pd.read_csv('./ml_model/X_csv.csv').drop(columns=["Unnamed: 0"])

    def predict(self,
                id: int = 0
                ):

        print('getting the random forest classifier prediction')

        pred = self.clf.predict(
            np.array(self.data.iloc[id]).reshape(1, -1)
        )

        print(pred)

        data = self.data.iloc[id]

        return pred, data

    def get_tree_rules(self):
        return tree.export_text(self.clf.estimators_[0],
                                feature_names=list(self.data.columns))
