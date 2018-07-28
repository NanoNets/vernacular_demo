import requests
import sys
import json

API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'

url = 'https://app.nanonets.com/api/v2/ImageCategorization/Model/'

MODEL_STATE_DICT = {-1: "Error in model training", 0:	"Model created. No training data uploaded yet", 1:	"Training data uploaded. Need to annotate data", 2:	"Training data annotated. Need to start training", 3:	"Model in training queue", 4:	"Model currently training", 5:	"Model hosted. Can be used for prediction"}

querystring = {'modelId': sys.argv[1]}

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(API_KEY,''), params=querystring)

print(response.text)

json_response = json.loads(response.text)
print "Model State:"
print MODEL_STATE_DICT[json_response["state"]]

