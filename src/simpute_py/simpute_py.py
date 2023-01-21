##package source code
def num_imputer(x,col,method):
    """
    Fill the empty values of a specific column with imputed values to facilitate data preprocessing.

    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe for imputing
    col: string
        name of the column to be imputed
    method: string
        A name of the imputing strategy. They include ['knn','quant_rand','mean','median','mode','bayes'], the default method is knn.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import num_imputer
    >>> num_imputer(row_df,'price','knn')
    """
    return

def cat_imputer(x,col,method):
    """
    Fill the empty values of a specific column with imputed values to facilitate data preprocessing.

    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy. They include ['knn','frequent','bayes', 'rand'], the default method is knn.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import cat_imputer
    >>> cat_imputer(row_df,'age_group','knn')
    """
    return

def bol_imputer(x,col,method):
    """
    Fill the empty values of a specific column with imputed values to facilitate data preprocessing.

    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy. They include ['knn','frequent','bayes', 'rand'], the default method is knn.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import bol_imputer
    >>> bol_imputer(row_df,'if_default_last_month','knn')
    """
    return

def all_imputer(x,method,cat_col):
    """
    Fill the empty values of the whole table with imputed values to facilitate data preprocessing.

    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
    method: string
        A name of the imputing strategy. They include ['knn','frequent','bayes', 'rand'], the default method is knn.
    cat_col: list
        A list of the names of all categorical columns in the dataframe.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing

    Examples
    ----------
    >>> from simpute import all_imputer
    >>> all_imputer(row_df,'knn', ['country', 'color'])
    """
    return
