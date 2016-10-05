from sklearn import linear_model
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html
def train_bayesian_ridge(x_train, y_train):
    # Picking model
    model = linear_model.BayesianRidge()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    return model.fit(x_train, y_train)


# http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
def train_support_vector_regression(x_train, y_train):
    # Picking model
    model = svm.SVR()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    return model.fit(x_train, y_train)


# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
def train_adaboost_dtr(x_train, y_train):
    # Picking model, this should be auto-selected down the road (hyperparameters)
    model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300)

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    return model.fit(x_train, y_train)
