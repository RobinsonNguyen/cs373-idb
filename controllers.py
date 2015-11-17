import json
import urllib
import subprocess

from urllib2.request import Request, urlopen, URLError

def politican_controller():
	politician_url = urllib.request.urlopen("http://politicianhub.me/api/v1/legislators")
	politicians = json.load(politician_url.read().decode('utf-8'))

	democratic_politicians = {}

	return democratic_politicians 