import pandas as pd
import seaborn as sns

def io_hw(out_path):
    ''' 
     Your input will be:
    
    out_path: a string that is the path to output a csv of the head of your data.
    
    Your outputs will be:
    
    df: The full pandas dataframe of your dataset.
    head_df: A new dataframe that is a copy of the first 5 lines of your dataframe, df.
    '''
    filepath = 'https://www.dropbox.com/s/egrqg5hcja6i5r5/ACSDATAFinal.csv?dl=0'
    df = pd.read_csv(filepath)
    head_df = df.head()
    output = head_df.to_csv(outpath)
    print(type(head_df))
    
    return df, head_df
