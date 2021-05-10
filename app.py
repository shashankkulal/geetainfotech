from flask import Flask, render_template, request, jsonify
import validators
from Geetainfotech import *

app = Flask(__name__)
key = "548d22495f4bbd2bd8cae8c2b804ffa4"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
	return render_template("game.html")

@app.route("/getTitle")
def title():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			t = getTitle(page)
			return jsonify(t)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getDescription")
def description():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			{"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getDescription(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getHeading")
def heading():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getHeading(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getRobots")
def robots():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getRobots(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getSitemap")
def sitemap():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getSitemap(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getAlt")
def alt():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getAlt(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getCanonical")
def canonical():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getCanonical(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getHttpStatus")
def httpc():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getHttpStatus(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getMixedContent")
def mix():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"Errors" : "Invalid Page Url"}
		else:
			d = getMixedContent(page)
			return jsonify(d)
	return {"Errors": "Unauthorized"}

@app.route("/getBroken")
def broken():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getBroken(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

@app.route("/getAll")
def gall():
	token = request.args.get("token")
	page = request.args.get("page_url")
	if token == key:
		if not validators.url(page):
			return {"errors": 1, "status": 400, "result": "Invalid Url"}
		else:
			d = getAll(page)
			return jsonify(d)
	return {"errors": 1, "status": 401, "result": "Un-Authorized"}

if __name__ == "__main__":
    app.run(debug = True)
