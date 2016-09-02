#!/usr/bin/env python

import requests
import json
from requests_oauthlib import OAuth1
from pprint import pprint


# main API URL
url = "http://jira url/rest/api/2"
s = requests.Session()

headers = {'Content-Type': 'application/json', 'Authorization' : 'token if you use that'}
response =  requests.get(url + '/search?jql=resolution%20=%20Unresolved%20order%20by%20priority%20DESC,updated%20DESC&startAt=0&maxResults=400', auth=('USERS', 'PASS')).json()

i=0
j=0
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

for value in traverse(response['issues']):
        #pprint (repr(value))

 for j in repr(value):
    print repr(value)[3]

#for i in response['issues']:
    # pprint (response['issues'][0]['fields']['description'])


# print the json
#print response.status_code
#pprint (json.dumps(response))
