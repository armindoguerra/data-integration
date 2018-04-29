import csv, sqlite3
import pandas, jsonify


# Creating database yawoen.db e table companies
con = sqlite3.connect("yawoen.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS companies;") 
cur.execute("CREATE TABLE companies (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name text, addressZip int, website text);") 

df = pandas.read_csv('q1_catalog.csv', sep=';')
df.to_sql('companies', con, if_exists='append', index=False)

con.close()
