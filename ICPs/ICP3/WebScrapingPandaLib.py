# ICP3

# Importing Required Libraries
import pandas as panda

# Pandas Basic Dataframes (Ref: https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm)
data = [1, 2, 3, 4, 5]
df = panda.DataFrame(data)
print(df)

print("------------------")

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = panda.DataFrame(data,columns=['Name','Age'])
print(df)

wikiURL = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

'''Reference: http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.read_html.html
read_html --> Reads Html into a list of DataFrame Objects
index_col  --> Column used to create the Index
attrs --> This is a dictionary of attributes that you can pass to use to identify the table in the HTML '''

wikitable = panda.read_html(wikiURL, index_col=0, attrs={'class': 'wikitable sortable plainrowheaders'})

# Printing the Wiki Table
print(wikitable)