
import pandas as pd
import os
import sys

#print(sys.path)

PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)

#from src.dataLoad.read_csv import LoadCSVToDataFrame

#print(PROJECT_DIR)
#BureauDataFrame1 = pd.DataFrame()

#BureauDataFrame1 = LoadCSVToDataFrame("train_credit_bureau_a_1_*")
#print(BureauDataFrame1.head())


def nullPercentage(df: pd.DataFrame, sort: bool = True, ascending: bool = False) -> pd.DataFrame:
    
    """
    Returns the percentage of null values for each column in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        sort (bool): Whether to sort the result by null percentage.
        ascending (bool): Sort order if sorting.

    Returns:
        pd.DataFrame: A DataFrame with columns 'column', 'nullCount', and 'nullPercent'.

    Note:
        Ensure to mention how this function works and which arguments are required.
    """

    totalRows = len(df)
    nullCounts = df.isnull().sum()
    nullPercents = (nullCounts / totalRows) * 100

    result = pd.DataFrame({
        'column': df.columns,
        'nullCount': nullCounts.values,
        'nullPercent': nullPercents.values
    })

    if sort:
        result = result.sort_values(by='null_percent', ascending=ascending)

    return result.reset_index(drop=True)



