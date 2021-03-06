# This file will be part of forcing models to have specific properties that govern
# their usage.


# These properties will help govern more advanced model selection based on relevance
# to the dataset or challenge.
class ModelProperties(object):

    def __init__(self, regression=False, online=False):
        self._classification = not regression  # I don't know if I should get fancy...
        self._regression = regression
        self._online_algorithm = online
