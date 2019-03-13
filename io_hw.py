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
    filepath = 'https://tufts.box.com/s/9auojpqiuidt5b8kb6e1vzmdy7l5h13l'
    df = pd.read_csv(filepath)
    head_df = df.head()
    output = head_df.to_csv(out_path)
    print(type(head_df))
    
    return df, head_df
