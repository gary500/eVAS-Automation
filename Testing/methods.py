import os
import xlsxwriter
from suds.client import Client

# Creates Directories
if not os.path.exists('order_function/'):
    os.makedirs('order_function/')
if not os.path.exists('master_function/'):
    os.makedirs('master_function/')

OrderDataURL = 'http://luswst007638:8080/eVASWS.ORDER/services/OrderPort?wsdl'
OrderDataClient = Client(OrderDataURL)
OrderDataMethods = [method for method in OrderDataClient.wsdl.services[0].ports[0].methods]
for i in OrderDataMethods:
    workbook = xlsxwriter.Workbook('order_function/' + i + '.xlsx')
    method = OrderDataClient.wsdl.services[0].ports[0].methods[i]
    params = method.binding.input.param_defs(method)
    print(i)
    parameters = [str(i[0]) for i in params]
    print(parameters)
    worksheet = workbook.add_worksheet()
    for index in range(0, len(parameters)):
        worksheet.write(0, index, str(parameters[index]))
    workbook.close()

MasterDataURL = 'http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?wsdl'
MasterDataClient = Client(MasterDataURL)
MasterDataMethods = [method for method in MasterDataClient.wsdl.services[0].ports[0].methods]
method = MasterDataClient.wsdl.services[0].ports[0].methods["getMasterDataServiceStatus"]
params = method.binding.input.param_defs(method)
for i in MasterDataMethods:
    workbook = xlsxwriter.Workbook('master_function/' + i + '.xlsx')
    method = MasterDataClient.wsdl.services[0].ports[0].methods[i]
    params = method.binding.input.param_defs(method)
    print(i)
    parameters = [str(i[0]) for i in params]
    print(parameters)
    worksheet = workbook.add_worksheet()
    for index in range(0, len(parameters)):
        worksheet.write(0, index, str(parameters[index]))
    workbook.close()
