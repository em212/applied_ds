import pandas as pd
import seaborn as sns
import pdb 

def io_hw(out_path):
    '''
    This is your homework assignment.
    You will be wrting a function here.
    
    Your input will be:
    
    out_path: a string that is the path to output a csv of the head of your data.
    
    Your outputs will be:
    
    df: The full pandas dataframe of your dataset.
    head_df: A new dataframe that is a copy of the first 5 lines of your dataframe, df.
    '''
    pdb.set_trace()
    df = pd.read_csv('⁨https://www.uscourts.gov/statistics/table/wire-a1/wiretap/2017/12/31')
    head_df = df.head()
    head_df.to_csv('~/Desktop/Term 4/Data Science/applied_ds.csv')
    return df, head_df