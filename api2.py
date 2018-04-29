import sqlite3
import pandas
from flask import jsonify,request,make_response,url_for,redirect
from json import dumps
import flask


app = flask.Flask(__name__) # Innit FLask
app.config["DEBUG"] = True # Activetion debug

# Route to Integrate filed website to yawoen.db
@app.route('/', methods=['GET','POST'])
def api2():
	if request.method == 'GET':
		return make_response('failure')
	if request.method == 'POST':

		# Revieving the parameters
		name = request.form['name']
		addresszip = request.form['addresszip']

		# Connecting in a database and making search
		conn = sqlite3.connect('yawoen.db')
		cur = conn.cursor()
		# The logic operator AND was used
		b = cur.execute("SELECT * FROM companies  WHERE name like '%{a}%' and addresszip = {b};".format(a=name,b=addresszip)).fetchall()
		b = pandas.DataFrame(b)
		json = {'id': str(b[0][0]),'name':str(b[1][0]),'zip':str(b[2][0]),'website':str(b[3][0])}

		response = json

		return jsonify(response)
	 
# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()