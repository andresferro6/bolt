import pandas as pd
from ydata_profiling import ProfileReport


try:
    df = pd.read_excel('data.xlsx')
    print(df.shape)
    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    profile.to_file("your_report.html")
except:
    breakpoint()
