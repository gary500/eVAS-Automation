# TODO read every testcase in every spreadsheet
# TODO use zeeps library to excecute the wsdl request

from zeep import Client

client = Client('http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort?wsdl', strict=False)
node = client.create_message(client.service, 'getLocations')
