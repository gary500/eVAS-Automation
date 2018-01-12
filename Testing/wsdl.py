import zeep

wsdl = 'http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.getLocations('1.2','9999','9999','1','1','','1','','11','11'))
