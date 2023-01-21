def date_imputer(input_df, col):
    input_df.loc[:,col] = input_df.loc[:,col].replace({None: datetime.today()})
    return input_df
