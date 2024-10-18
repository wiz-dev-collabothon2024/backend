import pandas as pd
import joblib
import numpy as np
from sklearn import tree


class RandomForestClassifier():
    def __init__(self,
                 n_estimators: int =100,
                 max_depth: int =None,
                 random_state: int =1
                 ):
        self.clf = joblib.load("./random_forest_classifier.joblib")
        self.data = pd.read_csv('./X_csv.csv').drop(columns=["Unnamed: 0"])

    def predict(self,
                id: int = 0
                ) -> float:

        pred = self.clf.predict(
            np.array(self.data.iloc[id]).reshape(1, -1)
        )

        return pred

    def get_tree_rules(self):
        return tree.export_text(self.clf.estimators_[0],
                                feature_names=list(self.data.columns))