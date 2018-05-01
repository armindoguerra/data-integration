# Data integration project

This project is composed of three steps. 

1. Was created a database with datas extracted from a csv file. 
2. was created a RESTful API to verify if some new data have match with database just created. If there are corresponding data in both sources the new ones are persisted in the database. 
3. Was created RESTful API to response a specific search with specified parameters. Details about all steps follow bellow.

The project was developed with python, Flask framework e sqlite database.

***To test the APIs it is mandatory to follow the order described bellow.***

## 1 - Load company data in a database

This step of the project consist in read data from file **q1_catalog.csv** and load into the database to create an entity named `companies`.

This entity contain the following fields: id, company name, zip code and website. The last field was created to second part of the project and therefore will not be fed in this step. The code to this is in **loadDb.py**. 

***This step is a prerequisite for the second step***

## 2 - An API to integrate data using a database

In this step was built an API to **integrate** `website` data field from **q2_clientData.csv** into the entity records we've just created using **HTTP protocol**. The data source doesn't provide the id field, so we used the zip code fields to aggregate the new attribute `website` and store it. The code to this is in **api.py**. 

***This step is a prerequisite for the third step***

## 3 - Matching API to get data based on specified parameters

In this final step we created an API to provide information from the entity for a client. The parameters used to capture information is `name` and `zip` code fields. The code to this also is in **api.py**.

# Prepare environment and run API´s (makefile)

To prepare the environment to run API it is necessary install some dependencies 
 ```
 $ pip install -r requirements.txt
 ```

Then just open a console and enter the command to create the database from the csv file. 
 ```
 $ python loadDb.py
 ```

To run the API type this command:
 ```
 $ python api.py
 ```

So, the datas are updated and it is possible to make requests to capture informations about the companies. The api is prepared to answer queries even when the inserted a piece of name the companies. In requests it is necessary send two parameter, `name` and `zip code` and the url is http://127.0.0.1:5000/queries.

The output should have this form:
 ```
 {
 	"id": 12,
 	"name": "Pizza Hut",
 	"zip": 10023,
 	"website": "www.pizzahut.com"
 }
 ```

The tests to code are in **test_api.py**. With api running, just run:
 ```
 $ python test_api.py
 ```
