import pandas as pd

ufo = pd.read_csv("http://bit.ly/uforeports")


# City      Colors Reported             Shape Reported          State               Time

ufo['Location'] = ufo['City'] + ufo['State']
print(ufo['Location'])
