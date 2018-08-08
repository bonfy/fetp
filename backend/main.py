# coding: utf-8

from flask import Flask, jsonify

app = Flask(__name__)

users = [{
    "name": "bonfy",
    "age" : 18,
},{
    "name": "kevin",
    "age" : 19,
}]

@app.route('/')
def home():
    return 'Hello World'

@app.route('/api/v1/users')
def get_users():
    return jsonify(dict(result=users))
