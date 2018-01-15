import zeep
import pandas as pd
import os

# TODO reading excel mechanisms to deal with two directories

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'addOrderRequest.xlsx')
directories = ['order_functions', 'master_functions']
for directory in directories:
    print(directory)
    # print(THIS_FOLDER)
    directory = os.path.join(THIS_FOLDER, directory)
    listing = os.listdir(directory)
    # print(listing)
    for infile in listing:
        my_file = os.path.join(directory, infile)
        # print(infile)
        print(my_file)
        df = pd.read_excel(my_file)
        rows = []
        for arr in df.as_matrix():
            rows.append(list(arr))
        print(*rows)

wsdl = 'http://www.webservicex.com/globalweather.asmx?wsdl'
client = zeep.Client(wsdl=wsdl, strict=False)
# print(client.service.GetCitiesByCountry(*rows))
