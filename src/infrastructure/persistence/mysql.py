import sys
#import mysql.connector
from mysql.connector.aio import connect
sys.path.append('src/application/ports')



def connect(**constants):
    return mysql.connector.connect(
        host=constants['host'],
        user=constants['user'],
        password=constants['password'],
        database=constants['database']
    )


def create(**constants):
    # MySQL Connection arguments
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": os.environ.get("MYPASS", ":("),
        "use_pure": True,
        "port": 3306,
    }
    # Connect to a MySQL server and get a cursor
    async with await connect(**config) as cnx:
        async with await cnx.cursor() as cur:
            # Execute a non-blocking query
            await cur.execute("SELECT version()")

            # Retrieve the results of the query asynchronously
            results = await cur.fetchall()
            print(results)
