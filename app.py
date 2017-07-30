import json

from flask import Flask
from flask import make_response, Response

from database import get_database_connection
app = Flask(__name__)

database_connection = get_database_connection()

@app.route('/health')
def route_health_check():
    return make_response('alive')

get_transaction_metrics_template = (
    "SELECT sub_key, timestamp, period, publish_transactions "
    "FROM transaction_metrics "
    "WHERE sub_key = '%s';"
)


@app.route('/transaction_metrics/<sub_key>', methods=['GET'])
def route_get_transaction_metrics(sub_key):
    sql = get_transaction_metrics_template % (sub_key)
    print "The sql is:"
    print sql
    cursor = database_connection.cursor()
    cursor.execute(sql)
    result = []
    for (sub_key, timestamp, period, publish_transactions) in cursor:
        result.append({
            "sub_key": sub_key,
            "timestamp": timestamp,
            "period": period,
            "publish_transactions": publish_transactions
        })
    cursor.close()
    flask_response = Response(json.dumps(result) + "\n", status=200, mimetype='application/json')
    return flask_response
    
