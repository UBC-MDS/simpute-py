import pytest
from simpute_py.bol_imputer import bol_imputer
import pandas as pd
import numpy as np

def test_bol_imputer():
    #Test imputing is working as expected
    test_df = pd.DataFrame({'bool_1': [True, False, False, "", "", "True", "False", 1, 0], 'bool_2':["","","","","",0,1,0,1]})
    bol_imputer(test_df, 'bool_1')
    solution_df_1 = pd.DataFrame({'bool_1': [True, False, False, False, False, "True", "False", 1, 0], 'bool_2':["","","","","",0,1,0,1]})
    assert test_df.equals(solution_df_1) == True, "Imputer is not working."

    #Testing imputer only changed column indicated
    assert solution_df_1['bool_2'].equals(test_df['bool_2']) == True, "Imputer is changing columns other than the one selected for imputation."

    #Testing edge case of the same frequencies of 'True' and 'False'
    bol_imputer(test_df, 'bool_2')
    solution_df_2 = pd.DataFrame({'bool_1': [True, False, False, False, False, "True", "False", 1, 0], 'bool_2':[True,True,True,True,True,0,1,0,1]})
    assert test_df.equals(solution_df_2) == True, "Imputer is not imputing 'True' when boolean frequencies are the same."

    #Test to check for any null values in the output
    assert test_df.isna().any().any() == False, "Imputer did not impute all null values of boolean columns"

    #Testing that the output is a dataframe
    assert isinstance(test_df, pd.DataFrame), "Imputer did not output a dataframe"
