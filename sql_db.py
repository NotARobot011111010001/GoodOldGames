# db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM games_info;')
        games = cursor.fetchall()
        if result > 0:
            got_games = jsonify(games)
        else:
            got_games = 'No Games in Database'
        return got_games


def create(game):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO games_info (name, developer, genre, tags) VALUES(%s, %s, %s, %s)',
                       (game["name"], game["developer"], game["genre"], game["tags"]))
    conn.commit()
    conn.close()
    