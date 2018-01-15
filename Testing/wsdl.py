import zeep

data = ['egypt', 'brazil']

wsdl = 'http://www.webservicex.com/globalweather.asmx?wsdl'
client = zeep.Client(wsdl=wsdl, strict=False)
print(client.service.GetCitiesByCountry(*data))
