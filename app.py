from flask import Flask, render_template, request, jsonify
import validators
from Geetainfotech import *

app = Flask(__name__)
key = "548d22495f4bbd2bd8cae8c2b804ffa4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getTitle')
def title():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			t = getTitle(page)
			t['status'] = 200
			return jsonify(t)
	return "Unauthorized"

@app.route('/getDescription')
def description():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getDescription(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

@app.route('/getHeading')
def heading():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getHeading(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

@app.route('/getRobots')
def robots():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getRobots(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

@app.route('/getSitemap')
def sitemap():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getSitemap(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

@app.route('/getAlt')
def alt():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getAlt(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

@app.route('/getCanonical')
def canonical():
	token = request.args.get('token')
	page = request.args.get('page_url')
	if token == key:
		if not validators.url(page):
			return "Invalide Page URL"
		else:
			d = getCanonical(page)
			d['status'] = 200
			return jsonify(d)
	return "Unauthorized"

if __name__ == '__main__':
    app.run(debug = True)
