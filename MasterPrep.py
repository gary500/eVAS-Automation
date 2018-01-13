import requests, os, xlsxwriter
from bs4 import BeautifulSoup


# TODO typo fix in 'getMasterDataServiceRequest' type

def finishing(last_element):
    last = requests.get('http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?xsd=eVASBasicTypes.xsd').text
    last_soup = BeautifulSoup(last, 'xml')
    original = last_element
    lastly = []
    end = []
    flag = 0
    for i in last_soup.find_all('complexType'):
        if not 'Type' in last_element:
            last_element += 'Type'
        if i['name'] == last_element:
            very_last = BeautifulSoup(str(i), 'xml')
            lastly = very_last.find_all('element')
            for name in lastly:
                end.append(name['name'])
            flag = 1
    if flag == 0:
        end.append(original)
    return end


def redirects(string, columns):
    elements = []
    txts = ''
    if string in outer.keys():
        for i in outer[string]:
            if i == 'unbounded':
                temp = redirects(outer[string][i], columns)
            if not i == 'unbounded':
                sequences = soup.find_all('complexType', attrs={'name': string})
                for sequence in sequences:
                    if '<xs:sequence maxOccurs="1" minOccurs="1">' in str(sequence):
                        last_elements = finishing(i)
                try:
                    for element in last_elements:
                        columns.append(element)
                except:
                    columns.append(i)
    return columns


# Creates MasterData spreadsheet Directory
if not os.path.exists('master_functions/'):
    os.makedirs('master_functions/')

functions = [
    'getLocationList',
    'setAccountLocations',
    'setAccounts',
    'getLocations',
    'setLocations',
    'getMasterDataServiceStatus',
    'getAccounts',
    'getAccountList'
]

# Parsing all the main functions from the WSDL
response = requests.get('http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?wsdl').text
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
response = requests.get('http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?xsd=eVASMasterDataReqRespTypes.xsd').text
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
    workbook = xlsxwriter.Workbook('master_functions/' + func + '.xlsx')
    worksheet = workbook.add_worksheet()
    temp = []
    columns = redirects(func, temp)
    for i in range(0, len(columns)):
        worksheet.write(0, i, str(columns[i]))
    workbook.close()
