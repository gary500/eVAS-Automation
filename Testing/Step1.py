import requests
from bs4 import BeautifulSoup

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
for func in sorted(functionTypes):
    print(func)
