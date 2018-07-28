import requests
import sys

API_KEY = 'AEajS8_Eomr4xyGMxKDpvubZ3XOf6BAGR_S3lEyAd6H'

url = 'https://app.nanonets.com/api/v2/ImageCategorization/Model/'

querystring = {'modelId': sys.argv[1]}

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(API_KEY,''), params=querystring)

print(response.text)