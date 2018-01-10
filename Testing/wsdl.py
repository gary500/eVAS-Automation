import zeep

wsdl = 'http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.addOrder('1.2','9999','9999','1','1','1','1','11','11','11','WebOrder','1000','2018-01-10-07:00',' 00:00:00.000-07:00','2018-01-15-07:00',' 2018-01-16-07:00','No','0','New Currency','US $1','100','10','1000'))

