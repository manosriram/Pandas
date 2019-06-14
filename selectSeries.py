import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")


# City      Colors Reported             Shape Reported          State               Time

# ufo['Location'] = ufo['City'] + ufo['State']

# print(ufo['Location'].head())

# Rename Columns

# ufo_cols = ["city", "colors reported",
# "shape reported", "state", "time", "location"]

# ufo.rename(columns={
#     'Colors Reported': 'Color_Reported',
#     'Shape Reported': 'Shape_Reported'
# }, inplace=True)

# OR

# ufo.columns = ufo_cols

# OR

ufo.columns = ufo.columns.str.replace(" ", "_")

print(ufo.head())
