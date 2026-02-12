import pandas as pd

def standard_col_names(df):
    """
    This function helps to standardize the dataframe column names. 
    """

    new_col_name = []
    for old_name in df.columns:
        name = old_name.strip().lower().replace(' ', '_')
        new_col_name.append(name)
    
    df.columns = new_col_name
    return df