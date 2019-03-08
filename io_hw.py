import pandas as pd
import seaborn as sns

def io_hw(out_path):
    '''
    This is your homework assignment.
    You will be writing a function here.
    '''
    file_place = "C:\Users\Vincent\Dropbox\College\Grad\Spring\Data Science\DataSets\project-sunroof-census_tract.csv"
    df = pd.read_csv(file_place)
    print(df)
    
    head_df = data.head(df)
    
    ''''
    Your input will be:
    
    out_path: a string that is the path to output a csv of the head of your data.
    
    Your outputs will be:
    
    df: The full pandas dataframe of your dataset.
    head_df: A new dataframe that is a copy of the first 5 lines of your dataframe, df.
    '''
    return df, head_df