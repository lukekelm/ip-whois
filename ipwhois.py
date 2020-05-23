import sys
import json
import requests

# Parse argument
pip = (sys.argv[1])

# Call to IP Geolocation API
request = requests.get('http://ip-api.com/json/' + pip)
response = request.json()

# Parse response
country = response['country']
regionname = response['regionName']
isp = response['isp']
atonsys = response['as']

print()
print('Country: ' + country)
print('Region: ' + regionname)
print('ISP: ' + isp)
print('AS: ' + atonsys)
print()
