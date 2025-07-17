
import pandas as pd

def drop_columns_by_name(df, *args, **kwargs):
    """
    Drops specified columns from a DataFrame using column names passed as *args.
    Additional keyword arguments (**kwargs) are forwarded to pandas' drop() method.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    *args: One or more column names to drop.
    **kwargs: Additional arguments to pass to df.drop(), e.g., inplace=True.

    Returns:
    pd.DataFrame or None: A new DataFrame with the columns dropped, or None if inplace=True.

    Note:
    To define how this function needs to work, mention **kwargs need to be parameters in the
    pandas drop function. Else, there would be an error in the function run.
    """
    columns_to_drop = list(args)
    return df.drop(columns=columns_to_drop, errors='ignore', **kwargs)