import ast
import jinja2
import os
import pydash
import urllib2
import webapp2

from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    autoescape=True,
    extensions=['jinja2.ext.autoescape'],
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname('oneclick0827'), 'templates'))
)

class DashboardHandler(webapp2.RequestHandler):
    url = "http://api108094sandbox.gateway.akana.com/IVRCCMaintenanceREST/account/transactionHistory"
    hardcodedData = {
        "transactionIdentifier": "0f8fad5b-d9cb-469f-a165-70867728950e",
        "messageIdentifier": "0f8fad5b-d9cb-469f-a165-70867728950e",
        "messageDateTime": "1999-05-31T13:20:00-05:00",
        "messageSequenceIdentifier": "1",
        "requestorInfo": {
            "serverIdentifier": "IVR",
            "componentIdentifier": "IVRMISC",
            "userIdentifier": {
                "name": "CredCardActAppIDDev",
                "parameters": {
                    "nameValuePair": {
                        "name": "CertSubjectDN",
                        "value": "cn=Client,ou=USB.COM,o=ESD,l=St. Paul,st=MN,c=US"
                    }
                }
            }
        },
        "ccTranHistoryRequest": {
            "ivrIdentifierData": {
                "requestingApplicationName": "CCIVR",
                "clientSource": "I",
                "serviceVersion": "1.0",
                "requestIdentifier": "testcase10"
            },
            "ccTranHistoryRequestData": {
                "accountNumber": "4081840012169457",
                "requestType": "StatementMonth",
                "statementMonth": "10",
                "tranSequence": "Reverse",
                "authIndicator": "ExcludeAuth",
                "continueNumber": "1",
                "maxItems": "10000000"
            }
        }
    }

    # TODO: Set as POST in the end
    def get(self):
        response = urlfetch.fetch(url=self.url,
                                  payload=self.hardcodedData,
                                  method=urlfetch.POST,
                                  headers={
                                      "Content-Type": "application/json",
                                      "Accept": "application/json"
                                  })

        if response.status_code == 200:
            template_values = {
                'debit': 0,
                'credit': 0
            }

            # Content
            content = ast.literal_eval(response.content)\
                .get('CCTranHistoryResponseData')\
                .get('TransactionDetails')\
                .get('TransactionData')

            # Iteration
            for transaction in content:
                amount = float(transaction['TransactionAmount'])

                if transaction.get('TransactionType') == 'Debit' and amount > 0:
                    template_values['debit'] += amount
                elif transaction.get('TransationType') == 'Credit' and amount > 0:
                    template_values['credit'] += amount

            # template = JINJA_ENVIRONMENT.get_template('dashboard.html')
            # self.response.write(template.render(template_values))
            self.response.write(template_values)
        else:
            self.response.write("Error Code: " + response.status_code)

