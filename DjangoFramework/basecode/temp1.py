import requests
import json

def apicall(request):

    import pandas as pd

    query1 = """
             {
              LmetaList(ledgerNo: 1) {
                id
                ledgerNo
                columnName
                columnType
              }
            }
            """

    result = requests.get('http://127.0.0.1:8100/graphql', json={'query': query1})
    json_data = json.loads(result.text)

    df_data = json_data['data']['LmetaList']

    df = pd.DataFrame(df_data)

