import mysql.connector

def getSqlConnection():
    config = {
        "user": "root",
        "host": "db",
        "port": "3306",
        "password": "pass",
        "database": "mytest",
        "auth_plugin": "mysql_native_password",
    }
    connection = mysql.connector.connect(**config)
    return connection