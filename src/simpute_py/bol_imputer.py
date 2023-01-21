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
