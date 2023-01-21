from simpute_py import num_imputer
import pytest
import pandas as pd

def test_num_imputer():
    df1=pd.read_csv(r'tesla_deaths.csv')
    col='Deaths'
    assert num_imputer.num_imputer(df1,col,'mode').isnull().sum()[list(df1.columns).index(col)]==0
    assert num_imputer.num_imputer(df1,col,'mean').isnull().sum()[list(df1.columns).index(col)]==0
    assert num_imputer.num_imputer(df1,col,method='median').isnull().sum()[list(df1.columns).index(col)]==0
    assert num_imputer.num_imputer(df1,col,method='knn').isnull().sum()[list(df1.columns).index(col)]==0
    assert num_imputer.num_imputer(df1,col).isnull().sum()[list(df1.columns).index(col)]==0
    
    # simpute_py.num_imputer(0,0,0)
    return 

