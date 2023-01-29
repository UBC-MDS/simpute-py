import datetime

def date_imputer(input_df, col):
    today = datetime.date.today()
    input_df[col] = input_df[col].replace({None: today})
    return input_df
