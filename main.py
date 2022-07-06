

import requests
import json
params = {
    "customerContact": "Ken David",
    "customerName": "CRM Consulting Inc",
    "innovativeRep": "rboyer@innovativesol.com",
    "newClient": "Existing",
    "sfdcEnvironment": "prod",
    "sfdcOppId": "0066f000012KBDyAAO",
    "sfdcPropId": "a226f000003LjcKAAS",
    "business_context": "In this case, we are pleased to have you say hello!",
    "environment1": "2",
    "environment2": "2",
    "environment3": "2",
    "autoFunding": True
  }
url = "https://59i75zdnlj.execute-api.us-east-2.amazonaws.com/Prod/generator/map/assess"
callAssessGenerator = requests.get(url, params=params)
print(callAssessGenerator)