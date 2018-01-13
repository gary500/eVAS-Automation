import pandas as pd
import requests
import lxml.etree as etree

df = pd.read_excel('addOrderData.xlsx', sheet_name='Sheet1')
messages = []
for i in range(1, len(df.columns)+1):
    url = "http://10.17.240.71:8080/eVASWS.ORDER/services/OrderPort"
    headers = {'content-type': 'text/xml'}
    body = """
    <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:v1='http://www.GGS.com/eVASServices/v1.0/'>
       <soapenv:Header>
          <v1:EVASSOAPHeader>
             <v1:TransactionIdentifier/>
             <v1:MessageSubmissionDateTime/>
             <v1:RequestorInfo/>
          </v1:EVASSOAPHeader>
       </soapenv:Header>
       <soapenv:Body>
          <v1:addOrderRequest>
             <v1:Version>1.2</v1:Version>
             <v1:UserID>9999</v1:UserID>
             <v1:Password>9999</v1:Password>
             <!--1 or more repetitions:-->
             <v1:Entries>
                <v1:SiteID>1</v1:SiteID>
                <v1:Client>1</v1:Client>
                <v1:AccountNumber>1</v1:AccountNumber>
                <v1:RTNo>1</v1:RTNo>
                <v1:AccountLocationID>11</v1:AccountLocationID>
                <v1:LocationNo>11</v1:LocationNo>
                <v1:LocationID>11</v1:LocationID>
                <v1:OrderEntry>Web Order</v1:OrderEntry>
                <v1:TotalAmount>1000</v1:TotalAmount>
                <v1:OrderDate>2018-01-10-07:00</v1:OrderDate>
                <v1:OrderTime>00:00:00.000-07:00</v1:OrderTime>
                <v1:ShipDate>2018-01-15-07:00</v1:ShipDate>
                <v1:DeliveryDate>2018-01-16-07:00</v1:DeliveryDate>
                <v1:Pending>No</v1:Pending>
                <v1:ATMCashAdd>0</v1:ATMCashAdd>
                <v1:ExtrefID/>
                <v1:ExtrefID2/>
                <v1:PassthruID xsi:nil='true' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'/>
                     <v1:MediaCategory>New Currency</v1:MediaCategory>
                      <v1:ItemType>
                         <v1:DenominationName>US $1</v1:DenominationName>
                         <v1:DenominationValue>100</v1:DenominationValue>
                      </v1:ItemType>
                      <v1:Count>10</v1:Count>
                      <v1:Amount>1000</v1:Amount>
                   </v1:OrderItems>
                </v1:OrderDenomData>
             </v1:Entries>
          </v1:addOrderRequest>
       </soapenv:Body>
    </soapenv:Envelope>""".format(df[i][0], df[i][1], df[i][2], df[i][3], df[i][4], df[i][5])

    response = requests.post(url, data=body, headers=headers)
    x = etree.fromstring(response.content)
    lines = etree.tostring(x, pretty_print=True).decode('UTF-8').splitlines()
    full_line = str([s for s in lines if "AddMessage" in s])
    pos1 = full_line.find('>')
    pos2 = full_line.find('</')
    message = full_line[pos1+1:pos2]
    messages.append(message)
    #print ("Request Sent")
result = pd.DataFrame({'Data': messages})
writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter')
result.to_excel(writer, sheet_name='Sheet1')
writer.save()
