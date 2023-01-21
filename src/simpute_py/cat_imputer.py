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
