import pymysql.cursors


class Database:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """
        This function open connection to your database.

        Args:
        None

        Returns:
        object from database or None in case of error.
        """
        try:
            connection = pymysql.connect(host=self.host,
                                         user=self.user,
                                         password=self.password,
                                         database=self.database,
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection

        except Exception as e:
            print(e)
            return None

    def insert(self, query):
        """
        This function insert record in table in your database.

        Args:
        query: sql statement for insertion.

        Returns:
        void.
        """

        connection = self.connect()

        if connection is None:
            return

        try:
            # sql = "INSERT INTO {} {} VALUES {}".format(
            #     table, columns, values)
            print(query)
            connection.cursor().execute(query)
            connection.commit()

        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            connection.close()

    def update(self, query):
        """
        This function update record in table in your database.

        Args:
        query: sql statement for update.

        Returns:
        void.
        """

        connection = self.connect()

        if connection is None:
            return

        try:
            # sql = "UPDATE {} SET {} WHERE {}".format(
            #     table, columns, where_clause)
            print(query)
            connection.cursor().execute(query)
            connection.commit()

        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            connection.close()

    def delete(self, table, where_clause):
        """
        This function delete record from table in your database.

        Args:
        table: table name.
        where_clause: condition to delete based on it .

        Returns:
        void.
        """

        connection = self.connect()

        if connection is None:
            return

        try:
            sql = "DELETE FROM {} WHERE {}".format(
                table, where_clause)
            print(sql)
            connection.cursor().execute(sql)
            connection.commit()

        except Exception as e:
            print(e)
            connection.rollback()

        finally:
            connection.close()


__all__ = ["Database"]
