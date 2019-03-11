import pandas as pd
import seaborn as sns

def io_hw(out_path):

    url="https://www.statistik-nord.de/fileadmin/Dokumente/Datenbanken_und_Karten/Stadtteilprofile/Stadtteilprofile-Berichtsjahre-2007-2016.xlsx"

    dfs = pd.read_excel(url,  None, encoding="utf8") # read in all excel sheets

    head_df = dfs["Berichtsjahr_2016"].head(5) # the data is organized into sheets post-import

    head_df.to_csv(out_path)

    return dfs, head_df
