
import pymysql.cursors

class Database(object):

    CONNECTION = None

    @staticmethod
    def get_connection(db_config=None):
        if Database.CONNECTION is None:
            try:
                db_host = db_config['DB_HOST']
                db_port = db_config['DB_PORT']
                db_user = db_config['DB_USER']
                db_password = db_config['DB_PASSWORD']
                db_name = db_config['DB_NAME']
                cursor = pymysql.cursors.DictCursor
                Database.CONNECTION = pymysql.connect(
                    host=db_host,
                    port=int(db_port),
                    user=db_user,
                    # password='auvLecfk9X',
                    password=db_password,
                    database=db_name,
                    cursorclass=cursor
                )
            except Exception as err:
                print(err)
                raise err
        return Database.CONNECTION
