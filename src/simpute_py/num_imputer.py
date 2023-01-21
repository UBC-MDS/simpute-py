
import pandas as pd
import numpy as np
from sklearn.feature_extraction import FeatureHasher
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
class KNN_num_imputer:
    def __init__(self,df=None):
        self.df=df
        self.dtype_dic=None
    def remove_id(self,df,numeric=[]):
        for col in numeric:
            if set(df[col]==sorted(df[col]))=={True}:
                # print(df[col])
                numeric.remove(col)
        return numeric
    def if_text(self,element):
        count=0
        for i in element:
            if i.isdigit():
                count+=1
        return count/len(element)<0.5
    def dtype_groupby(self,df,categoric=[]):
        numeric=list(df.select_dtypes(include=[np.number]).columns.values)
        numeric=self.remove_id(df,numeric)
        remain=list(df.columns)
        # remain.remove(target)
        text=[]
        drop=[]
        for i in numeric+categoric:
            remain.remove(i)
        for j in remain:
            if isinstance(df[j][0],(str)) and self.if_text(df[j][0]):
                text.append(j)
            else:
                drop.append(j)
        return {'numeric':numeric,'text':text,'drop':drop,'categoric':categoric} 
    def fit_transform(self,categoric=[]):
        #dtype group by
        df=self.df
        dtype_dic=self.dtype_groupby(df,categoric)
        numeric_feature,categoric_feature, drop_feature,text_feature=dtype_dic['numeric'],dtype_dic['categoric'],dtype_dic['drop'],dtype_dic['text']
        
        ##preporcessor for numeric
        preprocessor = make_column_transformer(
        (StandardScaler(), numeric_feature),
        # (CountVectorizer(stop_words="english"), text_feature),
        (OneHotEncoder(),categoric_feature),
        ("drop", drop_feature))
        X_train_proced=preprocessor.fit_transform(df)
        if isinstance(X_train_proced,(np.ndarray)):
            df_proced=pd.DataFrame(X_train_proced,columns=preprocessor.get_feature_names_out())
        else:
            df_proced=pd.DataFrame(X_train_proced.todense(),columns=preprocessor.get_feature_names_out())
        imputer = KNNImputer(n_neighbors=3)
        filled_df=imputer.fit_transform(df_proced)
        filled_df=pd.DataFrame(filled_df,columns=preprocessor.get_feature_names_out())
        preprocessor.output_indices_
        result=df.copy()
        result[numeric_feature] =filled_df.iloc[:,preprocessor.output_indices_['standardscaler']]
        # result.isnull().sum()
        self.dtype_dic=dtype_dic
        return result
    def get_dtype_dic_out(self):
        return self.dtype_dic

class Sun_switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False
 
    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
def num_imputer(x,col,method=None):
    """
    Fill the empty values of a specific column with imputed values to facilitate data preprocessing.
    Parameters
    ----------
    x: pandas dataframe
        A pandas dataframe for imputing
    col: string
        name of the column to be imputed
    method: string
        A name of the imputing strategy. They include ['knn','mean','median','mode'], the default method is mean.
    Returns
    ----------
    y: pandas dataframe
        A pandas dataframe after imputing
    Examples
    ----------
    >>> from simpute import num_imputer
    >>> num_imputer(row_df,'price','knn')
    """
    #set default method
    if method==None or method=='mean':
        target_name=col
        target_col=x[target_name]
        emp_index=target_col[target_col.isnull()].index
        emp_df=x.iloc[emp_index,:]
        result=x.copy()
        result.iloc[emp_index,:]=x[target_name].mean()
        return result
    
    v=method
    for case in Sun_switch(v):
        if case('median'):
            target_name=col
            target_col=x[target_name]
            emp_index=target_col[target_col.isnull()].index
            emp_df=x.iloc[emp_index,:]
            result=x.copy()
            result.iloc[emp_index,:]=x[target_name].median()
            return result
            break
        if case('mode'):
            target_name=col
            target_col=x[target_name]
            emp_index=target_col[target_col.isnull()].index
            emp_df=x.iloc[emp_index,:]
            result=x.copy()
            result.iloc[emp_index,:]=x[target_name].mode()[0]
            return result
            break
        if case('knn'):
            KNN= KNN_num_imputer(x)
            return KNN.fit_transform()
            break
        if case(): 
            #default mean impute method
            print("method value wrong,the recent methd are ['knn','mean','median','mode'], the default method is mean.")
            # No need to break here, it'll stop anyway
            
def testData_reader(path):
    df1=pd.read_csv(path)
    return df1
