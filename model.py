
import pandas as pd
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def buildModel(result_val):
    bank_data = pd.read_csv('bankruptcy-prev.csv')
    X = bank_data.iloc[:,0:6].values
    y = bank_data.iloc[:,6]
    result = []

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    model=LinearSVC()
    model.fit(X_train,y_train)
    prediction = model.predict(X_test)

    accuracyScore = accuracy_score(y_test, prediction)
    result.append(accuracyScore)
    result.append(model.predict(result_val)[0])
    return result


def train(result):
    res = []
    res.append(result)
    return buildModel(res)
