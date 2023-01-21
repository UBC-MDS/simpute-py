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
