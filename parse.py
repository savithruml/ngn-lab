#!/usr/bin/env python

import json, requests

def main():

	req_call = requests.get("http://ngn-lab.herokuapp.com/api/ngn/bad")
	#print req_call
	req_data = json.loads(req_call.text)
	#print good_bad
	good_bad = req_data['site']['id']
	print str(good_bad)

if __name__ == '__main__':
	main()
