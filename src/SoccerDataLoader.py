import sqlite3
import pandas as pd


class SoccerDataLoader:

    def __init__(self, database_path):
        self.database_path = database_path
        conn = sqlite3.connect(self.database_path)
        print("Connecting to the SQLite database...")

        # List of tables you're interested in
        tables = ["Player", "Team", "Match", "League"]

        # Load each table into a DataFrame and store it in a dictionary
        self.data = {}
        for table in tables:
            query = f"SELECT * FROM {table};"
            self.data[table] = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()
        print("Connection closed.")

    def load_data_with_query(self, query) -> pd.DataFrame:
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_path)

        # Query all rows from the table of interest
        query = query

        # Execute the query and convert the result to a DataFrame
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        return df

    def load_data(self, table_name) -> pd.DataFrame:
        # Connect to the SQLite database
        print("Connecting to the SQLite database...")
        conn = sqlite3.connect(self.database_path)

        # Query all rows from the table of interest
        query = f"SELECT * FROM {table_name}"

        # Execute the query and convert the result to a DataFrame
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        return df