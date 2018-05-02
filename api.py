import sqlite3
import pandas
from flask import jsonify,request,make_response,url_for,redirect
import flask


app = flask.Flask(__name__) # Innit FLask
app.config["DEBUG"] = False # Activetion debug

# Integrate filed website to yawoen.db
@app.route('/', methods=['GET'])
def api():
	conn = sqlite3.connect('yawoen.db')
	cur = conn.cursor()

	# Converting connection result in a pandas data frame to better manipulate datas
	r = cur.execute('SELECT * FROM companies;').fetchall()
	df1 = pandas.DataFrame(r, columns=['id', 'name', 'addresszip', 'website'])
	df2 = pandas.read_csv('q2_clientData.csv', sep=';')
	df3 = df1.merge(df2, on=['addresszip'])
	dfwebsiteId = df3.loc[:, ['id', 'website_y']]
	dfwebsiteId = dfwebsiteId.set_index('id')

	# Updating website values
	[cur.execute("UPDATE companies SET website =   ?  WHERE id =   ?;", (dfwebsiteId.website_y.loc[x], x)) for x in dfwebsiteId.index]
	r = cur.execute('SELECT * FROM companies;').fetchall()

	conn.commit()
	conn.close()

	return jsonify({'OK': 'yawoen.db is Updated!'})

# Make queries about companies
@app.route('/queries', methods=['POST'])
def api2():

	# Receiving the parameters
	name = request.form['name']
	addresszip = request.form['addresszip']

	# Connecting in a database and making search
	conn = sqlite3.connect('yawoen.db')
	cur = conn.cursor()

	# The logic operator AND was used
	b = cur.execute("SELECT * FROM companies  WHERE name like '%{a}%' and addresszip = {b};".format(a=name,b=addresszip)).fetchall()
	b = pandas.DataFrame(b)
	json = {'id': str(b[0][0]),'name':str(b[1][0]),'zip':str(b[2][0]),'website':str(b[3][0])}

	return jsonify(json)
	 
if __name__ == "__main__":
    app.run(debug=True)
