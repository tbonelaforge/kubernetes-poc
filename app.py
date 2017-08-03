import json

import os

from flask import Flask
from flask import make_response, Response, jsonify

from database import Database
app = Flask(__name__)

db_config = {
    "DB_HOST" : os.environ['DB_HOST'],
    "DB_PORT" : os.environ['DB_PORT'],
    "DB_USER" : os.environ['DB_USER'],
    "DB_PASSWORD" : os.environ['DB_PASSWORD'],
    "DB_NAME" : os.environ['DB_NAME']
}

database_connection = Database.get_connection(db_config)

@app.route('/health')
def route_health_check():
    return jsonify({"status": "alive"})

get_transaction_metrics_template = (
    "SELECT * "
    "FROM transaction_metrics "
    "WHERE sub_key = '%s';"
)


@app.route('/transaction_metrics/<sub_key>', methods=['GET'])
def route_get_transaction_metrics(sub_key):
    sql = get_transaction_metrics_template % (sub_key)
    cursor = database_connection.cursor()
    cursor.execute(sql)
    result = []
    for row in cursor:
        result.append(row)
    cursor.close()
    return jsonify(result)
    
