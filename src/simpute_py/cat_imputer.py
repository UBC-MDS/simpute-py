import pandas as pd
import numpy as np

def cat_imputer(x,col):
    """
    Fill the empty values of a specific column with the most frequent category to facilitate data preprocessing.

    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
    col: string
        name of the column waiting for imputing
       Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import cat_imputer
    >>> cat_imputer(row_df,'age_group')
    """

    # check for bad input
    if not isinstance(x, pd.DataFrame):
        raise TypeError("Please pass in a Pandas DataFrame for `x`")
    if x.empty:
        raise ValueError("DataFrame cannot be empty")
    if col not in x.columns:
        raise Exception("The given column does not exist in the dataframe.")

    x[col].fillna(value=x[col].
                  value_counts().
                  index[0],
                  inplace =True)
    return x
