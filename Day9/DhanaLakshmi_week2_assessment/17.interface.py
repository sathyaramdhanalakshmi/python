from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting data into SQL: {data}")

    def update(self, data):
        print(f"Updating data in SQL: {data}")

    def delete(self, data):
        print(f"Deleting data from SQL: {data}")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting data into NoSQL: {data}")

    def update(self, data):
        print(f"Updating data in NoSQL: {data}")

    def delete(self, data):
        print(f"Deleting data from NoSQL: {data}")


sql_db = SQLDatabase()
no_sql_db = NoSQLDatabase()

sql_db.insert("SQL Data")
no_sql_db.update("NoSQL Data")
