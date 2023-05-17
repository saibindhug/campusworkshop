"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7m5l269vf5qb8vtf0-a.oregon-postgres.render.com",
        database="todo_ilm5",
        user="todo_ilm5_user",
        password="IaIVzBzzWYqZKba6pe9dbkO69oeGbMNx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
