import pandas
import datetime
import time


def date_to_timestamp(date_datetime):
    """ Convert a date into an epoch timestamp value

    Args:
        date_datetime (datetime.date): date value

    Returns:
        float: unix epoch timestamp value
    """
    if pandas.isnull(date_datetime):
        return None
    elif isinstance(date_datetime, datetime.date):
        return time.mktime(date_datetime.timetuple())
    else:
        return None

def date_imputer(input_df, col):
    """ Imputation method for date type column

    Args:
        input_df (Pandas.DataFrame): input dataframe
        col (string): Name of the date column that needs imputation

    Returns:
        Pandas.DateFrame: dateframe after imputation of the dedicated column
    """
    date_series = input_df[col]
    epoch_timestamp_series = date_series.apply(date_to_timestamp)
    min_epoch_timestamp = epoch_timestamp_series.min()
    max_epoch_timestamp = epoch_timestamp_series.max()
    median_epoch_timestamp = (min_epoch_timestamp + max_epoch_timestamp)/2
    median_date = datetime.date.fromtimestamp(median_epoch_timestamp)
    input_df[col] = input_df[col].replace({None: median_date})
    return input_df
