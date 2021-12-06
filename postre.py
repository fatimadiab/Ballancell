import requests
import json
api_url = "http://localhost:5000/handle"
datas = { "type" : "Single Battery", "org_id" : "rmFT75nxhWsHSkTpo" ,"bem_id":"PyTBT56vqaPt22mZ2", "email":"fatima.om11@gmail.com ", "start":1635778688185, "end":1636383488185} 
headers = {"content-type":"application/json"}

response = requests.post(api_url, data=json.dumps(datas), headers=headers)
response.json()
response.status_code