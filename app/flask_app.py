from flask import Flask, make_response, request, jsonify
from flask import render_template, jsonify
import sqlite3

from app.stores_search_result import StoresSearchResult

def start_flask_app(config = {}):
  flask_app = Flask(__name__)
  flask_app.config = flask_app.config | config # Requires Python >= 3.9

  @flask_app.route('/', methods=['GET'])
  def index():
    return render_template('index.html')

  @flask_app.route('/search', methods=['GET'])
  def search():
    conn = sqlite3.connect(flask_app.config['DB_PATH'])
    query_parameters = request.args
    text = query_parameters.get('text')
    limit = int(query_parameters.get('limit', default=0))
    offset = int(query_parameters.get('offset', default=0))

    search_result = StoresSearchResult(conn, text, limit, offset)
    response = make_response(jsonify(search_result.get_results()), 200)
    return response

  flask_app.run()