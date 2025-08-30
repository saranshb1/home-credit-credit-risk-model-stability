
import pandas as pd
import polars as pl
import glob
import os

#dataPath = "E:/home-credit-credit-risk-model-stability/csv_files/train"

#df1 = pl.read_csv(dataPath+"/train_credit_bureau_a_1_0.csv")

#print(df1.describe())


def LoadCSVToDataFrame(prefix: str = "filename_a_1_") -> pd.DataFrame:
    """
    Load multiple CSV files with a specific prefix from a fixed folder
    into a single pandas DataFrame.

    Args:
        prefix (str): Prefix of the filenames to match (default: 'filename_a_1_').

    Returns:
        pd.DataFrame: Concatenated DataFrame of all matched CSV files.
    """
    # Fixed folder path
    data_path = "E:/home-credit-credit-risk-model-stability/csv_files/train/"  
    #data_path = os.path.join(os.getcwd(), "/train/")

    # Pattern like './data/filename_*.csv'
    file_pattern = os.path.join(data_path, f"{prefix}*.csv")
    csv_files = glob.glob(file_pattern)

    #print(csv_files)

    if not csv_files:
        raise FileNotFoundError(f"No files found matching pattern: {file_pattern}")

    df_list = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    """, ignore_index=True"""

    return combined_df


BureauDataFrame1 = LoadCSVToDataFrame("train_credit_bureau_a_1_*")
print(BureauDataFrame1.head())

