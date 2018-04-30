import flask
import flask_restful
import sqlite3
import pandas
import jsonify


app = flask.Flask(__name__)
api = flask_restful.Api(app)

class Api(flask_restful.Resource):
    def get(self):
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

        conn.commit()
        conn.close()

        return jsonify({'OK': 'yawoen.db is Updated!'})

api.add_resource(Api, '/')

if __name__ == "__main__":
    app.run(debug=False)