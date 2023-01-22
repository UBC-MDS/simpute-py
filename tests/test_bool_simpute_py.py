import pytest
from bol_imputer import bol_imputer
import pandas as pd
import numpy as np

def test_impute_freq():
    #Test imputing is working as expected
    test_df = pd.DataFrame({'bool_1': [True, False, False, "", "", "True", "False", 1, 0], 'bool_2':["","","","","",0,1,0,1]})
    bol_imputer(test_df, 'bool_1')
    solution_df_1 = pd.DataFrame({'bool_1': [True, False, False, False, False, "True", "False", 1, 0], 'bool_2':["","","","","",0,1,0,1]})
    assert test_df.equals(solution_df_1) == True, "Imputer is not working."

    #Test imputing on edge case of the same frequencies
    bol_imputer(test_df, 'bool_2')
    solution_df_2 = pd.DataFrame({'bool_1': [True, False, False, False, False, "True", "False", 1, 0], 'bool_2':[True,True,True,True,True,0,1,0,1]})
    assert test_df.equals(solution_df_2) == True, "Imputer is not working."

    #Test for to check for any null values
    assert test_df.isna().any().any() == False, "Imputer did not impute all null values"

def test_exception_cases():
    """Test cases where input is incorrect"""
    test_df = pd.DataFrame({'bool_1': [True, False, False, "", "", "True", "False", 1, 0]})

    with pytest.raises(Exception):
        bol_imputer(df=None, col='bool_1')
    with pytest.raises(Exception):
        bol_imputer(df=test_df, col=None)
    with pytest.raises(Exception):
        bol_imputer(df=test_df, col='Non_existant_column')