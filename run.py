import os
from app.flask_app import start_flask_app
from app.stores_data_parser import StoresDataParser
from app.stores_database import StoresDatabase

STORES_JSON_FILEPATH = 'app/static/json/stores.json'

script_dir = os.path.dirname(__file__)
json_file_path = os.path.join(script_dir, STORES_JSON_FILEPATH)

stores_parser = StoresDataParser(json_file_path, ("name","postcode"))
stores_db = StoresDatabase('shopsDB', stores_parser.get_data())
db_file_path = stores_db.initialize()

start_flask_app({"DB_PATH": db_file_path})
