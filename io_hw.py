import pandas as pd

def io_hw(out_path):
<<<<<<< HEAD

    url="https://www.statistik-nord.de/fileadmin/Dokumente/Datenbanken_und_Karten/Stadtteilprofile/Stadtteilprofile-Berichtsjahre-2007-2016.xlsx"

    dfs = pd.read_excel(url,  None, encoding="utf8") # read in all excel sheets

    head_df = dfs["Berichtsjahr_2016"].head(5) # the data is organized into sheets post-import

    head_df.to_csv(out_path)

    return dfs, head_df
=======
    '''
    This is your homework assignment.
    You will be wrting a function here.
    
    Your input will be:
    
    out_path: a string that is the path to output a csv of the head of your data.
    
    Your outputs will be:
    
    df: The full pandas dataframe of your dataset.
    head_df: A new dataframe that is a copy of the first 5 lines of your dataframe, df.
    '''
    filePath = 'https://tufts.app.box.com/file/411860624841'
    df = pd.read_csv(filePath, sep = ',', error_bad_lines=False)
    head_df = df.head()
    output = head_df.to_csv(out_path, sep = ',')
    print(type(head_df))
    return df, head_df
>>>>>>> upstream/master
