import zeep

data = ['1.3', 'GSI', 'Glory']
wsdl = 'http://luswst007638:8080/eVASWS.MASTERDATA/services/MasterDataPort?wsdl'
client = zeep.Client(wsdl=wsdl, strict=False)
print(client.service.getMasterDataServiceStatus(*data))
