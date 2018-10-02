import json
import mysql.connector as connector
from mysql.connector import errorcode

try:
    with open('config.json') as config:
        c = json.load(config)
        cnx = connector.connect(
            user = c['user'],
            password = c['password'],
            host = c['host'],
            database = c['database']
        )
except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("ERROR: Failed to connect with given credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("ERROR: Database does not exist")
    else:
        print(err)
else:
  cnx.close()
