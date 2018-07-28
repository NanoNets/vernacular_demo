import requests
import sys

API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'
url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/'

data = {'urls' : [sys.argv[2]], 'modelId': ('', sys.argv[1])}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth(API_KEY, ''), files=data)

print(response.text)