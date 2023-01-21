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
