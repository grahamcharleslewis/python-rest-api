import psycopg2
from config import config

class Database:
    def __init__(self):
        print("Creating database instance...")
        self.db_conn = self.connect()
        
    def connect(self):
        conn = None
        try:
            params = config()

            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.db_conn is not None:
            self.db_conn.close()
            print('Database connection closed.')

    def get_db_version(self):
        cur = self.db_conn.cursor()
    
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        
        cur.close()
