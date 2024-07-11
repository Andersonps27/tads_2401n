import pandas as pd
import sqlite3

data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
})

conn = sqlite3.connect('mydatabase.db')

data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

conn.close()

conn sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute( f"""
    DELETE FROM {table name}
    WHERE {query}
""")

conn.client()

conn = sqlite3.connect('mydatabase.db')

query = """
    SELECT Name
    From client
    WERE name ID ('Alice', 'Bob', 'Charlie', 'David')
"""