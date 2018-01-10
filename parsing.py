import requests, os, csv, xlsxwriter
from bs4 import BeautifulSoup

def redirects(str, columns):
    # print(str)
    if str in outer.keys():
        for i in outer[str]:
            if i == 'unbounded':
                # print(outer[str][i])
                temp = redirects(outer[str][i], columns)
                # print(temp)
                # break
            if not i == 'unbounded':
                print(i)
                columns.append(i)
        return columns

if not os.path.exists('order_functions/'):
    os.makedirs('order_functions/')

functions = [
    'getOrderProfile',
    'updateStandingOrder',
    'getLocations',
    'addOrder',
    'getOrderExtract',
    'updatePassthru',  # Typo that Jeffery will fix it later
    'getOrderDeatilsList',  # Typo that Jeffery will fix it later
    'getOrderDetailsList',
    'getOrderStatus',
    'getOrder',
    'verifyLocationPassword',
    'getOrderServiceStatus',
    'updateOrderStatus',
    'updatePassthruID',
    'updateOrder',
    'getStandingOrder',
    'getAccounts',
    'getOrderSummaryList',
    'getShipDateFromDeliveryDate',
    'getDeliveryDateFromShipDate',
    'addStandingOrder'
]

response = requests.get('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?wsdl').text
messages_soup = BeautifulSoup(response, 'xml')
messages = messages_soup.find_all('wsdl:message')
# print(types)
functionTypes = []
for message in messages:
    if str(message['name']).replace('Request', '') in functions:
        # functionTypes.append(message['name'])
        parts_soup = BeautifulSoup(str(message), 'xml')
        parts = parts_soup.find_all('part')
        for part in parts:
            # print(message['name'] + " => " + part['element'][4:])
            functionTypes.append(str(part['element']).replace('tns:', ''))
# for func in sorted(functionTypes):
# print(func)

response = requests.get('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?xsd=eVASOrdersReqRespTypes.xsd').text
# print(resp)
functions = []
inner = {}
outer = {}
soup = BeautifulSoup(response, 'xml')
names = soup.find_all('schema')
for name in names:
    Complex = name.find_all('complexType')
    if Complex:
        for i in Complex:
            functions.append(i['name'])
complexes = soup.find_all('complexType')
if len(Complex) == len(functions):
    for i in range(0, len(Complex)):
        inner = {}
        types = BeautifulSoup(str(Complex[i]), 'xml')
        # print('\n' + functions[i])
        for attr in types.find_all('element'):
            # print(attr['name'] + " :: " + str(attr['type']).replace('tns:', '').replace('xs:', ''))
            try:
                if attr['maxOccurs'] == 'unbounded':
                    inner[attr['maxOccurs']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
            except:
                inner[attr['name']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
        # print(inner)
        outer[functions[i]] = inner
print(outer)

for func in sorted(functionTypes):
    workbook = xlsxwriter.Workbook('order_functions/' + func + '.xlsx')
    worksheet = workbook.add_worksheet()
    print('*** ' + func + ' ***')
    temp = []
    columns = redirects(func, temp)
    print(columns)
    for i in range(0, len(columns)):
        worksheet.write(0, i, str(columns[i]))
    print("\n")
    workbook.close()

