from sklearn import linear_model
from modules.toolbox import framework_tools as ft

#
# I apologize for my variable and function names, will fix in the future (to Alex)
# ^^ If that doesn't happen I owe you 50 bucks
#
# There is also some repetitive code in terms of fitting and scoring models, this will
# likely be split out into a new helper
#

def run_SGDRegressor(path, filename):
    X_train, X_test, y_train, y_test = ft.get_TrainTest(path, filename)

    # Picking model
    model = linear_model.SGDRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(X_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(X_test, y_test)


def run_PassiveAggressiveRegressor(path, filename):
    X_train, X_test, y_train, y_test = ft.get_TrainTest(path, filename)

    # Picking model
    model = linear_model.PassiveAggressiveRegressor()

    # Training the model. "partial_fit" can be used to train the model one chunk of data at a time.
    model.fit(X_train, y_train)

    # Scores the model using the coefficient of determination R^2 of the prediction.
    return model.score(X_test, y_test)

