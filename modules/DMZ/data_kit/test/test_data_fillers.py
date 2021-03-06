from unittest import TestCase
from modules.DMZ.data_kit import data_io
from modules.DMZ.data_kit import data_filler
import path_handler
import numpy as np
import pandas as pd


class TestDataFilling(TestCase):

    def setUp(self):
        self.data = data_io.get_data(path_handler.get_test_data() + "unittest_data.csv")
        self.data["Nonsense"] = np.nan
        self.data = self.data.apply(pd.to_numeric, errors='coerce')
        self.data.loc[self.data.shape[0]] = [np.nan] * self.data.shape[1]
        self.target = 'target'
        self.start = self.data.shape

    def standard_drop(self, result, orientation, message):
        # Act
        end = result.shape

        # Assert
        self.assertLess(end[orientation], self.start[orientation], msg=message)

    def test_drop_missing_data_rows(self):
        self.standard_drop(data_filler.drop_missing_data_rows(self.data, .99), 0, "Failed to remove any rows")

    def test_drop_missing_data_columns(self):
        self.standard_drop(data_filler.drop_missing_data_columns(self.data, .99), 1, "Failed to remove any columns")

    def test_drop_all_missing_data_columns(self):
        self.standard_drop(data_filler.drop_all_missing_data_columns(self.data), 1, "Failed to remove any columns")

    def test_drop_all_missing_data_rows(self):
        self.standard_drop(data_filler.drop_all_missing_data_rows(self.data), 0, "Failed to remove any rows")

    def test_fill_missing_data(self):
        # Act
        data = data_filler.fill_missing_data(self.data, 7)

        # Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")

    def test_fill_missing_data_average(self):
        # Act
        data = data_filler.drop_all_missing_data_columns(self.data)
        data = data_filler.fill_missing_data_average(data)

        # Assert
        self.assertFalse(data.isnull().values.any(), msg="Failed to replace all NaNs")
