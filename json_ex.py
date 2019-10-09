import requests

import urllib.request

r = urllib.request.urlopen('https://www.google.com')



u = r.getcode()


print(u)

print(r.read())
##location = 'delhi technological university'
##
##pa = {'address': location}
##print(url1)
##r = requests.get( url = url1, params = pa)
##
##data = r.json()
##
##print(data)
