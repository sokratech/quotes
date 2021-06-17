import mysql.connector


class QuotesDatabase:
    def __init__(self, host="127.0.0.1", user="root", password="", database="quotes", max_length=101):
        self._host = host
        self._user = user
        self._password = password
        self._dbname = database
        self._max_length = max_length
        self._database = self._connect()
        self._cursor = self._get_cursor()

    def get_quote(self):
        stmt = "SELECT id, zitat AS quote, autor_herkunft_thema AS origin FROM zitate WHERE CHAR_LENGTH(zitat) < {} " \
               "ORDER BY RAND() LIMIT 1;".format(self._max_length)
        self._cursor.execute(stmt)
        return self._cursor.fetchall()[0]

    def _connect(self):
        return mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._dbname
        )

    def _get_cursor(self):
        return self._database.cursor()
