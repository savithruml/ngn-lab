#!/usr/bin/env python
from flask import Flask, jsonify, abort

app=Flask(__name__)

site = [
	{
		'id': u'good',
		'Subject': u'Next-Generation-Networks',
		'Code': u'TLEN 5838-003',
		'Owner': u'Interdisciplinary Telecom Program - University of Colorado Boulder',
		'Status': u'Yes, this website works!'
	},
	
	{
		'id': u'bad',
		'Subject': u'Next-Generation-Networks',
		'Code': u'TLEN 5838-003',
		'Owner': u'Interdisciplinary Telecom Program - University of Colorado Boulder',
		'Status': u'No, this website doesnt work!'
	}
]

@app.route('/')
def index():
	
	return 'Goto /api/ngn/<good/bad>'
	
@app.route('/api/ngn/<id>', methods=["GET"])
def data(id):
	
	if len(id) == 0:
		abort(404)
	elif str(id) == 'good':
		return jsonify({'site': site[0]})
	elif str(id) == 'bad':
		return jsonify({'site': site[1]})
	else:
		abort(404)
	
if __name__=="__main__":
	app.run(debug=True)
