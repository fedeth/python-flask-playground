import sqlite3

DEFAULT_SQL_CREATE_STORES_TABLE = """
    CREATE TABLE IF NOT EXISTS stores (
      id integer PRIMARY KEY,
      name text NOT NULL,
      postcode text NOT NULL
    );
  """

class StoresDatabase:
  def __init__(self, db_name, data):
    self.db_name = db_name
    self.__data = data

  def initialize(self):
    conn = sqlite3.connect(f'{self.db_name}.db', isolation_level=None) # autocommit mode

    if conn != None:
      self.__create_table(conn, DEFAULT_SQL_CREATE_STORES_TABLE)
    else:
      print("Error. Cannot create the database connection.")
      
    self.__clear_data(conn, 'DELETE FROM stores')
    self.__load_data(conn)
    conn.close()

    # initialization returns the DB file path
    return f'{self.db_name}.db'
  
  def __clear_data(self, conn, delete_statement):
    self.__conn_execute(conn, delete_statement)
 
  def __load_data(self, conn):
    sql = '''
      INSERT INTO stores(name,postcode)
      VALUES(?,?)
    '''
    c = conn.cursor()
    for entry in self.__data:
      c.execute(sql, (entry['name'], entry['postcode']))
    c.close()
  
  def __create_table(self, conn, sql_create_table_statement):
      self.__conn_execute(conn, sql_create_table_statement)

  def __conn_execute(self, conn, command):
    c = conn.cursor()
    c.execute(command)
    c.close()
  