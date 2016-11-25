import os
import sys

sys.path.insert(0, os.path.abspath('../../../..'))

from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import text_handler
import setup

import pandas as pd
from sklearn import preprocessing
from modules.toolbox.data_package import DataPackage
from modules.toolbox.validation_package import ValidationPackage


class TestDataFilling(TestCase):

    def setUp(self):
        self.data = data_io.get_data(setup.get_datasets_path(), "titanic_train.csv")

    def test_text_column_to_numeric(self):

        # Arrange
        column = self.data["Sex"]

        # Act
        self.data["Sex"] = text_handler.text_column_to_numeric(column)

        # Assert
        self.assertTrue(self.data["Sex"].dtype != "object", msg="Failed to convert text to categorical values")

    def test_convert_dataframe_text(self):
        # Act
        data = text_handler.convert_dataframe_text(self.data, .5)

        # Assert
        self.assertTrue(data["Sex"].dtype != "object" and data["Name"].dtype == "object",
                        msg="Converted incorrect features")

    def test_convert_nonpredictive_text(self):
        # Act
        data = text_handler.convert_nonpredictive_text(self.data)

        # Assert
        self.assertTrue(data["Name"].isnull, msg="Failed to convert text to NaN")