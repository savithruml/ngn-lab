#!/usr/bin/env python

from flask import Flask, jsonify, abort, redirect, Response, Markup

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

@app.after_request
def author(response):
	
	response.headers['Author'] = 'Savithru M Lokanath, Dr.Levi Perigo'
	response.headers['Contact'] = 'savithru at colorado dot edu'
	return response

@app.route('/')
def index():
	
	return Markup('<h2>Goto /api/ngn/<good/bad></h2>')

@app.route('/api/')
def minion():
	
	return redirect('http://24.media.tumblr.com/130f821e0c1c0ba7490622aa870ffe96/tumblr_n4iuliOlHb1tziei6o1_500.gif')
	
@app.route('/api/ngn/')
def parameters():
	
	return Markup('<h2>Add /good OR /bad to the request URL</h2>')

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
