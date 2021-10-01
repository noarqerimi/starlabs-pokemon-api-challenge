# Starlabs Pokemon API Challenge
## Introduction
This API has been built using Python 3 and Flask, moreover the application contains Swagger by default which allows easy to use UI interface to interact with the API.

### Build instructions

#### Database
Install PostgreSQL on the target system.

Run the following SQL queries to create the database and users for the Pokemon application:

```
CREATE DATABASE pokemondb;
CREATE USER pokemonuser WITH PASSWORD 'pokemonpassword';
GRANT ALL PRIVILEGES ON DATABASE "pokemondb" TO "pokemonuser";
```

#### Install Application Specific Libraries
While Pokemon API was built using Python 3, install pip for Python 3 i.e. `sudo apt install python3-pip`

Using pip3 install the following libraries:

```
pip3 install flask
pip3 install flask_restx
pip3 install psycopg2
pip3 install csv
pip3 install json
```

#### Run the application

Database configuration is stored on a file called `config.json`, this contains host, port, username and password of the database, edit this file with the local server before running the application.

Run the application as a typical Flask application by using the following command: `FLASK_APP=app.py flask run` and it will expose the application on localhost port 5000 as follows `http://127.0.0.1:5000/`, open the URL in the browser to interact with Swagger.

