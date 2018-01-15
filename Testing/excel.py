import pandas as pd
import os

# TODO reading excel mechanisms to deal with two directories

# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'addOrderRequest.xlsx')
# print(my_file)

df = pd.read_excel('addOrderRequest.xlsx', sheet_name='Sheet1')
rows = []
for arr in df.as_matrix():
    rows.append(list(arr))

print(rows)