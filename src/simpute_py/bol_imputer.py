import pandas as pd
import numpy as np

def bol_imputer(df,col,method='mode'): #How is the user converting their data into a df? 
    """
    Fill the empty values of a specific column with imputed values to facilitate data preprocessing.

    Parameters
    ----------
    df: pandas dataframe
        A pandas dataframe waiting for imputing
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy. They include ['mode'] or most frequent value.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import bol_imputer
    >>> bol_imputer(row_df,'if_default_last_month','knn')
    """
    
    bool_col = df[col]

    #Replace any empty fields with nan
    bool_col.replace('', np.nan, inplace=True)

    #Check if the column does have null values
    if bool_col.isnull().sum() == 0:
        return print("The selected column does not have any missing values to impute.")

    #Check if the column is boolean
    if (bool_col.dropna().isin([True, False, 1, 0, 'True', 'False'])).all() == False:
        return print("The selected column is not Boolean, please select another column.")

    #Calculate frequencies of boolean values
    count_true = 0
    count_false = 0

    for bool in bool_col.dropna():
        if bool in [True, 'True', 1]:
            count_true += 1
        else:
            count_false += 1
    
    freq_true = count_true/len(bool_col.dropna())
    freq_false = count_false/len(bool_col.dropna())

    #Select high frequency value
    if freq_true == freq_false or freq_true > freq_false:
        impute_value = True 
    else:
        impute_value = False
    
    #Replace null values with 
    df[col].fillna(impute_value, inplace = True)

    return df
