##package source code
def num_imputer(x,col,method):
    """
    Fill the empty values of a specific column with missing values to facilitate data preprocessing.
    
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
   
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy,ont of the methods ['knn','quant_rand','mean','medien','mode','bayes'],default method is knn.
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
    Fill the empty values of a specific column with missing values to facilitate data preprocessing.
    
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
   
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy,ont of the methods ['knn','frequent','bayes'],default method is knn.
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
    Fill the empty values of a specific column with missing values to facilitate data preprocessing.
    
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
   
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy,ont of the methods ['knn','frequent','bayes'],default method is knn.
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

def date_imputer(x,col,method):
    """
    Fill the empty values of a specific column with missing values to facilitate data preprocessing.
    
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
   
    col: string
        name of the column waiting for imputing
    method: string
        A name of the imputing strategy,ont of the methods ['knn','frequent','bayes','mean','median'],default method is knn.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing   
        
    Examples
    ----------
    >>> from simpute import date_imputer
    >>> date_imputer(row_df,'trans_day','knn')
    """
    return 

def all_imputer(x,method):
    """
    Fill the empty values of the whole table with missing values to facilitate data preprocessing.
    
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe waiting for imputing
    method: string
        A name of the imputing strategy,ont of the methods ['knn','frequent','bayes'],default method is knn.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing   
        
    Examples
    ----------
    >>> from simpute import all_imputer
    >>> all_imputer(row_df,'knn')
    """
    return 