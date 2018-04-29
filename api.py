import flask
from flask import jsonify, json
import sqlite3
import pandas


app = flask.Flask(__name__) # Innit FLask
app.config["DEBUG"] = True # Activetion debug

# Route to Integrate filed website to yawoen.db
@app.route('/', methods=['GET'])
def api():
	
	# Connecting in a database yawoen.db
	conn = sqlite3.connect('yawoen.db')
	cur = conn.cursor()
	    
	# Converting connection result in a pandas data frame to better manipulate datas
	r = cur.execute('SELECT * FROM companies;').fetchall()
	df1 = pandas.DataFrame(r, columns=['id','name','addresszip', 'website'])
	df2 = pandas.read_csv('q2_clientData.csv', sep=';')
	df3 = df1.merge(df2, on=['addresszip'])
	dfwebsiteId = df3.loc[:, ['id','website_y']]
	dfwebsiteId = dfwebsiteId.set_index('id')

	# Updating wbsite values
	[cur.execute("UPDATE companies SET website =   ?  WHERE id =   ?;", (dfwebsiteId.website_y.loc[x], x)) for x in dfwebsiteId.index]

	# Printing datas in Route
	res = cur.execute('SELECT * FROM companies;').fetchall()
	
	conn.commit()
	conn.close()

	return jsonify(res) 

	 
# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()