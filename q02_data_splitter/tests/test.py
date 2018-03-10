import unittest
from inspect import getfullargspec
from ..build import q02_data_splitter as student
from greyatomlib.time_series_101_project.q02_data_splitter.build import q02_data_splitter as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('q02_data_splitter/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q02_data_splitter/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q02_data_splitter/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q02_data_splitter/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/perrin-freres-monthly-champagne.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_args(self):
        self.args_student = getfullargspec(self.student_func).args
        self.args_original = getfullargspec(self.solution_func).args
        self.assertEqual(len(self.args_student), len(self.args_original),
                         "Expected argument(s) %d, Given %d" % (len(self.args_original), len(self.args_student)))

        # check the defaults of the function



    def test_return_dataframe(self):
        assert_frame_equal(self.student_return[0], self.original_return[0],
                           obj="The return values do not match expected values")
    def test_return_dataframe_1(self):
        assert_frame_equal(self.student_return[1], self.original_return[1],
                           obj="The return values do not match expected values")

