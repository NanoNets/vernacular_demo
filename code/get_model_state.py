import requests
import sys
import json

API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'

url = 'https://app.nanonets.com/api/v2/ImageCategorization/Model/'

MODEL_STATE_DICT = {-1: "Error in model training", 0:	"Model created. No training data uploaded yet", 1:	"Training data uploaded. Need to annotate data", 2:	"Training data annotated. Need to start training", 3:	"Model in training queue", 4:	"Model currently training", 5:	"Model hosted. Can be used for prediction"}

querystring = {'modelId': sys.argv[1]}

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(API_KEY,''), params=querystring)

json_response = json.loads(response.text)
print MODEL_STATE_DICT[json_response["state"]]

if json_response["state"]==3 or json_response["state"]==4:
	print "please wait for the model to finish training, try again in 5 minutes"
if json_response["state"]==5:
	print "The model is ready to test run the command:"
	print "python code/predict_file.py",sys.argv[1],"images/HindiJokes/0.jpg" 
	print "or"
	print "python code/predict_url.py",sys.argv[1],"https://i.pinimg.com/originals/63/91/7d/63917d7eba98cb1ce837e78bc9f8afc9.jpg" 

