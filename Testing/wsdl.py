from suds.client import Client

client = Client('http://luswst007638:8080/eVASWS.ORDER/services/OrderPort?wsdl')
try:
    print(client.service.getOrderProfile([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.updateOrderStatus([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.addOrder([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrder([1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrderExtract([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getLocDeliWeekDays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.updateOrder([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.updathruID([1, 1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrderStatus([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getShipDateFromDeliveryDate([1, 1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getAccounts([1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.updateStandingOrder([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrderDetailsList([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.addStandingOrder([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrderServiceStatus([1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.verifyLocatiword([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getDeliveryDateFromShipDate([1, 1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getStandingOrder([1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getLocations([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getOrderSummaryList([1, 1, 1, 1]))
except Exception as e:
    print(e)

client = Client('http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?wsdl')
try:
    print(client.service.getMasterDataServiceStatus([1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.setAccountLocations([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.setAccounts([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.setLocations([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getAccounts([1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getLocationList([1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getAccountList([1, 1, 1, 1]))
except Exception as e:
    print(e)
try:
    print(client.service.getLocations([1, 1, 1, 11, 1, 1, 1, 1, 1, 1]))
except Exception as e:
    print(e)
