from bs4 import BeautifulSoup
import requests

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

