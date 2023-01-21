import datetime

def date_imputer(input_df, col):
    today = datetime.date.today()
    input_df.loc[:,col] = input_df.loc[:,col].replace({None: today})
    return input_df
