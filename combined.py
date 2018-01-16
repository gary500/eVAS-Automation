import zeep, os
import pandas as pd
import sys, string


class CodeGeneratorBackend:
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return "".join(self.code)

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise(SyntaxError, "internal error in code generator")
        self.level = self.level - 1

# TODO reading excel mechanisms to deal with two directories
# TODO work on the zeep function to make it dynamic

c = CodeGeneratorBackend()
c.begin(tab="    ")
c.write("from suds.client import Client\n")
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
directories = ['order_function', 'master_function']
for directory in directories:
    if directory == 'order_function':
        wsdl = 'http://luswst007638:8080/eVASWS.ORDER/services/OrderPort?wsdl'
        c.write("\nclient = Client('" + wsdl + "')\n")
    elif directory == 'master_function':
        wsdl = 'http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?wsdl'
        c.write("\nclient = Client('" + wsdl + "')\n")
    directory = os.path.join(THIS_FOLDER, directory)
    listing = os.listdir(directory)
    for infile in listing:
        my_file = os.path.join(directory, infile)
        df = pd.read_excel(my_file)
        rows = []
        for arr in df.as_matrix():
            rows.append(list(arr))
        c.write("try:\n")
        c.indent()
        c.write("print(client.service." + infile.replace('.xlsx', '') + "(" + str(*rows) + "))\n")
        c.dedent()
        c.write("except Exception as e:\n")
        c.indent()
        c.write("print(e)\n")
        c.dedent()
print(c.end())
