import mysql.connector
from mysql.connector import Error

from project.scraper.db.data_to_save import DataToSave

class Db:

    @staticmethod
    def insert_recent_blocks():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='blockchain',
                                                 user='root',
                                                 password='root')

            mySql_insert_query = """INSERT INTO blocks (height, hash, mined_date, size) 
                                   VALUES (%s, %s, %s, %s) """

            records_to_insert = DataToSave.get_blocks()

            cursor = connection.cursor()
            cursor.executemany(mySql_insert_query, records_to_insert)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into blocks table")

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")