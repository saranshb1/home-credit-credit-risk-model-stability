
import pandas as pd

def describeDataFrame(reader_function, *args, **kwargs):
    """
    Takes a CSV reader function, loads the DataFrame, and prints summary information.

    Args:
        reader_func (function): Function that returns a DataFrame.
        *args, **kwargs: Arguments passed to the reader_func.

    Returns:
        pd.DataFrame: The loaded DataFrame (optional, for further processing).
    """

    #This reader_function will take in outputs from the defined function in the code and
    #return the necessary values
    df = reader_function(*args, **kwargs)

    print("✅ DataFrame Loaded Successfully!\n")
    print("📐 Shape:", df.shape)
    print("\n🔍 Column Types:")
    print(df.dtypes)
    
    print("\n📊 Basic Statistics:")
    print(df.describe(include='all').transpose())

    """print("\n🧼 Null Value Summary:")
    nullSummary = df.isnull().sum()
    nullPercent = (nullSummary / len(df)) * 100
    print(pd.DataFrame({
        'null_count': nullSummary,
        'null_percent': nullPercent
    }).sort_values(by='null_percent', ascending=False))
    """
    return df  # Optional return



#from folderA.read_csv import LoadCSVToDataFrame
#from folderB.data_analysis.describeDatasets import describeDataFrame  # or wherever you place the wrapper

#describeDataFrame(LoadCSVToDataFrame, prefix="train_credit_bureau_a_1_")

