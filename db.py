import psycopg2
import csv
import json

host = ''
username = ''
password = ''
database = ''
port = 5432

with open("config.json") as config_file:
    config = json.load(config_file)
    for item, value in config["postgresql"].items():
        if item == 'host':
            host = value
        elif item == 'username':
            username = value
        elif item == 'password':
            password = value
        elif item == 'database':
            database = value
        elif item == 'port':
            port = value

db_connection = psycopg2.connect(f"dbname='{database}' user='{username}' password='{password}' host='{host}' port={port}")

class Database:
    def __init__(self):
        self.init_seed_data()

    def init_seed_data(self):
        cursor = db_connection.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS pokemon
                        (id integer, name VARCHAR(255), type VARCHAR(255), type1 VARCHAR(255), total integer, hp integer, 
                        attack integer, defense integer, sp_attack integer, sp_def integer, 
                        speed integer, generation integer, legendary boolean) ''')
        cursor.execute(f'DELETE FROM pokemon;')
        with open('data/pokemon.csv') as csv_file:
             pokemon_csv_reader = csv.reader(csv_file, delimiter=',')
             for row in pokemon_csv_reader:
                cursor.execute(f'''INSERT INTO pokemon (id, name, type, type1, total, hp, attack, defense, sp_attack, sp_def, speed, generation, legendary) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                                        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]))
        db_connection.commit()

    def sortBy(self, column, order, limit):
        orderKeyword = 'ASC'
        sql_statement = ""
        cursor = db_connection.cursor()

        if limit is None:
            limit = 100

        if order is None:
            order = 'ascending'

        if order.lower() == 'ascending':
            orderKeyword = 'ASC'
        elif order.lower() == 'descending':
            orderKeyword = 'DESC'
        else:
            return "Please specify 'Ascending' or 'Descending' order."


        if not column:
            sql_statement = (f"\tSELECT row_to_json(pokemon) FROM pokemon ORDER BY id {orderKeyword} LIMIT {limit}")
        else:
            if column.lower() == 'id' or column.lower() == 'name':
                sql_statement = (f"\tSELECT row_to_json(pokemon) FROM pokemon ORDER BY {column} {orderKeyword} LIMIT {limit}")
            else:
                return "Only order by id or by name is allowed."
        cursor.execute(sql_statement)
        result = cursor.fetchall()
        return list(result)

    def filterBy(self, pokemonType):
        cursor = db_connection.cursor()
        if pokemonType is None:
            return "Please provide Pokemon type."

        cursor.execute(f"SELECT row_to_json(pokemon) FROM pokemon WHERE type = '{pokemonType}';")
        result = cursor.fetchall()
        return list(result)

    def returnAll(self):
        cursor = db_connection.cursor()

        cursor.execute(f"SELECT row_to_json(pokemon) FROM pokemon;")
        result = cursor.fetchall()
        return list(result)


    def __delete__(self):
        db_connection.close()