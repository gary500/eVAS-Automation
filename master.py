#Author: Gary Lambsar

import requests
import lxml.etree as etree
import pandas as pd

messages = []

for i in range(5):

    url="http://10.17.240.60:8080/eVASWS.MASTERDATA/services/MasterDataPort"
    headers = {'content-type': 'text/xml'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://www.GGS.com/eVASServices/MasterDataService/v1.0/">
       <soapenv:Header>
          <v1:EVASSOAPHeader>
             <v1:TransactionIdentifier>?</v1:TransactionIdentifier>
             <v1:MessageSubmissionDateTime>?</v1:MessageSubmissionDateTime>
             <v1:RequestorInfo>?</v1:RequestorInfo>
          </v1:EVASSOAPHeader>
       </soapenv:Header>
       <soapenv:Body>
          <v1:setAccountsRequest>
             <v1:Version>2.0</v1:Version>
             <v1:UserID>30</v1:UserID>
             <v1:Password>3000</v1:Password>
             <!--Zero or more repetitions:-->
             <Account>
                <v1:ClientNumber>30</v1:ClientNumber>
                <v1:AccountNumber>302</v1:AccountNumber>
                <v1:RTN>30</v1:RTN>
                <v1:SecondRTN>30</v1:SecondRTN>
                <v1:Name>A300</v1:Name>
                <v1:BusinessDesc/>
                <v1:Address/>
                <v1:Address2/>
                <v1:City/>
                <v1:State/>
                <v1:ZIP/>
                <v1:PhoneNumber>0000000000</v1:PhoneNumber>
                <v1:FaxNo>0000000000</v1:FaxNo>
                <v1:Email/>
                <v1:TaxID>30</v1:TaxID>
                <v1:SubjectToCount>No</v1:SubjectToCount>
                <v1:BagIDExpAcct>No</v1:BagIDExpAcct>
                <v1:AuxOnUSMask/>
                <v1:DepProcessInformation/>
                <v1:DBA/>
                <v1:Status>Deposit and Orders</v1:Status>
                <v1:AccountProfile>1</v1:AccountProfile>
                <v1:ValidationProfile>-1</v1:ValidationProfile>
                <v1:JournalProfile>1</v1:JournalProfile>
                <v1:UseLocSubAccts>No</v1:UseLocSubAccts>
                <v1:CTReportLimits>
                   <v1:DepositLimit>10000</v1:DepositLimit>
                   <v1:WithdrawLimit>10000</v1:WithdrawLimit>
                </v1:CTReportLimits>
                <v1:AccountType/>
                <v1:DepositType/>
                <v1:MiscellaneousData>
                   <v1:MiscID1/>
                   <v1:MiscID2/>
                   <v1:MiscID3/>
                   <v1:MiscID4/>
                   <v1:MiscID5/>
                   <v1:MiscID6/>
                   <v1:MiscID7/>
                   <v1:MiscID8/>
                   <v1:MiscID9/>
                </v1:MiscellaneousData>
                <v1:AcctProcessingProfiles>
                   <v1:DirectProcessingProfile>-1</v1:DirectProcessingProfile>
                   <v1:LoggedBagProcessingProfile>-1</v1:LoggedBagProcessingProfile>
                   <v1:UnverifiedMediaProcessingProfile>-1</v1:UnverifiedMediaProcessingProfile>
                   <v1:ATMProcessingProfile>-1</v1:ATMProcessingProfile>
                   <v1:OrderVerificationProfile>-1</v1:OrderVerificationProfile>
                   <v1:WithdrawProfile>-1</v1:WithdrawProfile>
                   <v1:BagID-MB-Profile>-1</v1:BagID-MB-Profile>
                   <v1:ProcessMeidaProfile>1</v1:ProcessMeidaProfile>
                   <v1:AnalysisProfile>0</v1:AnalysisProfile>
                </v1:AcctProcessingProfiles>
                <v1:OrderConfig>0</v1:OrderConfig>
                <v1:OrderLimits>
                   <v1:MaximumAmount>99999999900</v1:MaximumAmount>
                   <v1:MinimumAmount>0</v1:MinimumAmount>
                   <v1:DailyMaximumAmount>99999999900</v1:DailyMaximumAmount>
                </v1:OrderLimits>
                <v1:IncomingShipments>
                   <v1:IncShipEntryMode>0</v1:IncShipEntryMode>
                   <v1:MaximumAmount>99999999900</v1:MaximumAmount>
                   <v1:MinimumAmount>0</v1:MinimumAmount>
                   <v1:DailyMaximumAmount>99999999900</v1:DailyMaximumAmount>
                </v1:IncomingShipments>
                <v1:ProductivityParams>
                   <v1:SetupTime>00:00:00</v1:SetupTime>
                   <v1:TransactionTime>00:00:00</v1:TransactionTime>
                   <v1:DollarPerHour>0</v1:DollarPerHour>
                   <v1:NotesPerHour>0</v1:NotesPerHour>
                </v1:ProductivityParams>
                <v1:CashForCashOrderParams>
                   <v1:CashForCashOrdAccount>No</v1:CashForCashOrdAccount>
                   <v1:CashForCashOrdType>Type1</v1:CashForCashOrdType>
                </v1:CashForCashOrderParams>
                <v1:AcctSubAccounts>
                   <v1:SubAccountNumber>3000</v1:SubAccountNumber>
                   <v1:SubRTNO>30</v1:SubRTNO>
                   <v1:PhoneNumber>0000000000</v1:PhoneNumber>
                   <v1:FaxNO>0000000000</v1:FaxNO>
                   <v1:Address/>
                   <v1:City/>
                   <v1:State/>
                   <v1:ZIP/>
                   <v1:Email/>
                   <v1:SubAccountTypeID>
                      <v1:Billing>No</v1:Billing>
                      <v1:Adjustment>No</v1:Adjustment>
                      <v1:Orders>No</v1:Orders>
                      <v1:Type4>No</v1:Type4>
                      <v1:MICR>No</v1:MICR>
                      <v1:Type6>No</v1:Type6>
                   </v1:SubAccountTypeID>
                </v1:AcctSubAccounts>
             </Account>
          </v1:setAccountsRequest>
       </soapenv:Body>
    </soapenv:Envelope>"""

    response = requests.post(url, data=body, headers=headers)

    x = etree.fromstring(response.content)

    lines = etree.tostring(x, pretty_print=True).decode('UTF-8').splitlines()

    full_line = str([s for s in lines if "SystemMessage" in s])

    pos1 = full_line.find('>')
    pos2 = full_line.find('</')

    message = full_line[pos1 + 1:pos2]

    messages.append(message)

result = pd.DataFrame({'Data': messages})

writer = pd.ExcelWriter('C:/Users/lambsarg/Desktop/results.xlsx', engine='xlsxwriter')

result.to_excel(writer, sheet_name='Sheet1')

writer.save()
