import sys
import os
import argparse
import nose

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Database

PARSER = argparse.ArgumentParser(description="Run Functional Tests.")


PARSER.add_argument('--service_host', default="http://localhost:5000", help="Where is the service running? (defaults to http://localhost:5000)")

PARSER.add_argument('--db_host', default="192.168.64.2", help="Where is the database running? (defaults to 192.168.64.2)")

PARSER.add_argument('--db_port', default="32639", help="What port is the database listening on? (defaults to 32639)")

PARSER.add_argument('--db_name', default="analytics", help="the name of the database within mysql (defaults to analytics)")

PARSER.add_argument('--db_password', default="auvLecfk9X", help="the database password (defaults to auvLecfk9X)")

PARSER.add_argument('--db_user', default='root', help="The user to user when logging into the database. (defaults to root)")

PARSER.add_argument('--log', action='store_const',
                    const=True, default=False,
                    help="Show logging.info() messages (default to False).")

PARSER.add_argument('nose_args', metavar='nose_arg', nargs='*',
                    help='Arguments to pass on to nosetests (default to running all tests).')


def write_nose_args(ftest_args):
    """
    @param ftest_args: The arguments given to the ftests.py script
    @return: an argument list suitable for passing directly to nosetests
    """
    final_nose_args = ['ftests.py', '--nocapture', '--tc=service_host:' + ftest_args.service_host, '--process-timeout=60']
    if ftest_args.log is False:
        final_nose_args.append('--nologcapture')
    final_nose_args += ftest_args.nose_args
    return final_nose_args

if __name__ == '__main__':
    ARGS = PARSER.parse_args()
    db_config = {
            "DB_HOST": ARGS.db_host,
            "DB_PORT": ARGS.db_port,
            "DB_NAME": ARGS.db_name,
            "DB_PASSWORD": ARGS.db_password,
            "DB_USER": ARGS.db_user
    }
    print "Connecting to the database host: %s ..." % (db_config['DB_HOST'])
    database_connection = None
    try:
        database_connection = Database.get_connection(db_config)
    except Exception as database_exception:
        print "There was a DatabaseException:"
        print database_exception
        exit(1)
    print "Running nosetests against host %s ..." % (ARGS.service_host)
    NOSE_ARGS = write_nose_args(ARGS)
    nose.main(argv=NOSE_ARGS)