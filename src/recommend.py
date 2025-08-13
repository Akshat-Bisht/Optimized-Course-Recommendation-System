import pandas as pd

def top_n_courses(df, n=5):
    return df.groupby('Course_Id')['Rating'].mean().sort_values(ascending=False).head(n)