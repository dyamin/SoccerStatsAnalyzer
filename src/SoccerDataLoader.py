import sqlite3

import pandas as pd


class SoccerDataLoader:

    def __init__(self, database_path):
        self.database_path = database_path
        conn = sqlite3.connect(self.database_path)
        print("Connecting to the SQLite database...")

        # List of tables you're interested in
        tables = ["Player", "Team", "Match", "League", "Player_Attributes"]

        # Load each table into a DataFrame and store it in a dictionary
        self.data = {}
        for table in tables:
            query = f"SELECT * FROM {table};"
            self.data[table] = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()
        print("Connection closed.")
