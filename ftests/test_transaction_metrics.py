from apitest import ApiTest

from database import Database

def test_get_transaction_metrics():
    insert_fixture_data()
    test = (
        ApiTest().transaction_metrics.get('test_sub_key').json()
    )
    results = test.value
    assert len(results) == 11
    all_have_sub_key(results, 'test_sub_key')
    delete_fixture_data()


def insert_fixture_data():
    database_connection = Database.get_connection()
    fd = open('fixtures/insert_test_transaction_metrics.sql', 'r')
    sql = fd.read()
    fd.close()
    cursor = database_connection.cursor()
    cursor.execute(sql)
    cursor.close()
    database_connection.commit()


def delete_fixture_data():
    database_connection = Database.get_connection()
    sql = "DELETE FROM transaction_metrics WHERE sub_key = 'test_sub_key';"
    cursor = database_connection.cursor()
    cursor.execute(sql)
    cursor.close()
    database_connection.commit()


def all_have_sub_key(results, sub_key):
    for result in results:
        assert result['sub_key'] == sub_key