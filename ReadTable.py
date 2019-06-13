import pandas as pd

user_cols = ["user_id", "age", "gender", "occupation", "zip_code"]

val = pd.read_csv("http://bit.ly/movieusers", sep="|", header=None, names=user_cols)
print(val.head())