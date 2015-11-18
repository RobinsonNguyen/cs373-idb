import json
import urllib2
import subprocess

def politician_controller():
	#politician_url = urllib.request.urlopen("http://politicianhub.me/api/v1/legislators")
	#politicians = json.load(politician_url.read().decode('utf-8'))

	req = urllib2.Request("http://politicianhub.me/api/v1/legislators")
	url = urllib2.urlopen(req)
	data = json.load(url)
	politicians = data['legislators']

	democratic_politicians = []

	for t in test:
		poli = {}
		for k, v in t.items():
			if(k == 'first_name')
				poli['firstName'] = v
			if(k == 'last_name')
				poli['last_name'] = v
			if(k == 'twitter')
				poli['twitter'] = v
			if(k == 'state')
				poli['state'] = v
			if(k == 'birthday')
				poli['birthday'] = v
		democratic_politicians.append(poli)

	return democratic_politicians 