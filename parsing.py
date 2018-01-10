import requests, os, xlsxwriter
from bs4 import BeautifulSoup

#TODO Fix the function name typos in the list "functions"

def redirects(str, columns):
    if str in outer.keys():
        for i in outer[str]:
            if i == 'unbounded':
                temp = redirects(outer[str][i], columns)
            if not i == 'unbounded':
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

# Parsing all the main functions from the WSDL
response = requests.get('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?wsdl').text
messages_soup = BeautifulSoup(response, 'xml')
messages = messages_soup.find_all('wsdl:message')
functionTypes = []
for message in messages:
    if str(message['name']).replace('Request', '') in functions:
        parts_soup = BeautifulSoup(str(message), 'xml')
        parts = parts_soup.find_all('part')
        for part in parts:
            functionTypes.append(str(part['element']).replace('tns:', ''))

# Getting the columns for every function Dynamically
response = requests.get('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?xsd=eVASOrdersReqRespTypes.xsd').text
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
Complexes = soup.find_all('complexType')
if len(Complex) == len(functions):
    for i in range(0, len(Complex)):
        inner = {}
        types = BeautifulSoup(str(Complex[i]), 'xml')
        for attr in types.find_all('element'):
            try:
                if attr['maxOccurs'] == 'unbounded':
                    inner[attr['maxOccurs']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
            except:
                inner[attr['name']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
        outer[functions[i]] = inner

# Writing the spreadsheets with the correct column names for every function
for func in sorted(functionTypes):
    workbook = xlsxwriter.Workbook('order_functions/' + func + '.xlsx')
    worksheet = workbook.add_worksheet()
    temp = []
    columns = redirects(func, temp)
    for i in range(0, len(columns)):
        worksheet.write(0, i, str(columns[i]))
    workbook.close()

