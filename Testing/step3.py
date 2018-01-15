import requests, os, xlsxwriter
from bs4 import BeautifulSoup

#TODO Fix the function name typos in the list "functions"

def finishing(last_element):
    last = requests.get('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?xsd=eVASBasicTypes.xsd').text
    last_soup = BeautifulSoup(last, 'xml')
    #print(last_soup)
    #print(last_element)
    #for last_element in last_list:
    #print(last_element)
    original = last_element
    lastly = []
    end = []
    flag = 0
    #print(last_element + "\n\n\n")
    for i in last_soup.find_all('complexType'):
        if not 'Type' in last_element:
            last_element += 'Type'
        if i['name'] == last_element:
            #print(i['name'])
            very_last = BeautifulSoup(str(i), 'xml')
            lastly = very_last.find_all('element')
            for name in lastly:
                end.append(name['name'])
            #print(end)
            flag = 1
    if flag == 0:
        end.append(original)
    #if len(lastly) > 0:
        #print(lastly)
    #for i in last_soup.find_all('complexType', attr={'name':'ItemType'}):
    #    print(i)
    #    if last_element in i:
    #        print(last_element)
    return end

def redirects(string, columns):
    elements = []
    txts = ''
    if string in outer.keys():
        for i in outer[string]:
            # print(i)
            if i == 'unbounded':
                #txts = ''
                temp = redirects(outer[string][i], columns)
            if not i == 'unbounded':
                #if not 'type' in i:
                #    txts += i + 'type'
                #else:
                #    txts = i
                #basicTypes = soup.find_all('xs:complexType', attrs={'name':txts})
                #for basicType in basicTypes:
                #    print(basicType)
                #    print('****************')
                sequences = soup.find_all('complexType', attrs={'name':string})
                for sequence in sequences:
                    #print(type(sequence))
                    #print(i)
                    if '<xs:sequence maxOccurs="1" minOccurs="1">' in str(sequence):
                        #elements.append(i)
                        last_elements = finishing(i)

                    #if elements:
                    #    elements = finishing(elements)
                try:
                    #print(elements)
                    #last_elements = finishing(elements)
                    for element in last_elements:
                        #print(string + "*****")
                        #print(element)
                        columns.append(element)
                except:
                    #print(string + "*****")
                    #print(i)
                    columns.append(i)
    #print(columns)
    #print()
    return columns

if not os.path.exists('order_function/'):
    os.makedirs('order_function/')

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
        #print(types.find_all('element'))
        for attr in types.find_all('element'):
            #print(attr)
            try:
                if attr['maxOccurs'] == 'unbounded':
                    inner[attr['maxOccurs']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
            except:
                inner[attr['name']] = str(attr['type']).replace('tns:', '').replace('xs:', '')
        outer[functions[i]] = inner
print(outer)
#print(outer['OrderAddType'])

# Writing the spreadsheets with the correct column names for every function
for func in sorted(functionTypes):
    workbook = xlsxwriter.Workbook('order_function/' + func + '.xlsx')
    worksheet = workbook.add_worksheet()
    temp = []
    columns = redirects(func, temp)
    for i in range(0, len(columns)):
        worksheet.write(0, i, str(columns[i]))
    workbook.close()

