import requests 
import json
from os import listdir
from os.path import isfile, join
import os 
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#need to define the api key and the list of categories
API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'
categories = ['HindiJokes', 'TeluguJokes', 'MarathiJokes', 'BengaliJokes']


#Create new model
url = 'https://app.nanonets.com/api/v2/ImageCategorization/Model/'
headers = {
    'accept': 'application/x-www-form-urlencoded'
}
data = {'categories' : categories}
response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(API_KEY, ''), data=data)
print(response.text)

#Get model_id once created
model_id = json.loads(response.text)["model_id"]

#Upload Training Images
url = 'https://app.nanonets.com/api/v2/ImageCategorization/UploadFile/'
for category in categories:
	images_path = join(dir_path,"images",category)
	images = [join(images_path, f) for f in listdir(images_path) if isfile(join(images_path, f))]
	for image in images:
		print "Uploading image", image
		data = {'file' :open(image, 'rb'),'category' :('', category), 'modelId' :('', model_id)}
		response = requests.post(url, auth= requests.auth.HTTPBasicAuth(API_KEY, ''), files=data)


#Train Model
url = 'https://app.nanonets.com/api/v2/ImageCategorization/Train/'
querystring = {'modelId': model_id}
response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth(API_KEY, ''), params=querystring)
print(response.text)

print "-x-x-x-x-x-x-x-x-x-"
print "Now run:"
print "python code get_model_state.py ", model_id