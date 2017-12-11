import unittest
from inspect import getargspec
from ..build import q01_load_data as student
from greyatomlib.time_series_101_project.q01_load_data.build import q01_load_data as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/perrin-freres-monthly-champagne.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_args(self):
        self.args_student = getargspec(self.student_func).args
        self.args_original = getargspec(self.solution_func).args
        self.assertEqual(len(self.args_student), len(self.args_original),
                         "Expected argument(s) %d, Given %d" % (len(self.args_original), len(self.args_student)))

        # check the defaults of the function



    def test_return_dataframe(self):
        assert_frame_equal(self.student_return, self.original_return,
                           obj="The return values do not match expected values")

