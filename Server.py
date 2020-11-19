from flask import Flask, request
import json

app = Flask(__name__)

with open('mock.json') as fp:
    jsonData = {'data': json.loads(fp.read())}

@app.route('/')
def base_route():
    return jsonData

@app.route('/post', methods=['POST'])
def post_route():
    return ({'message': 'You successfully posted'}, 200)

@app.route('/post2', methods=['POST'])
def post_route2():
    return ({'message': 'You successfully posted','body': request.get_json()}, 200)

@app.route('/post3', methods=['GET','POST'])
def get_post_route():
    if request.method == 'GET':
        return ({'message': 'You choose to GET instead of POST'}, 200)
    else:
        return ({'message': 'You choose to POST instead of GET'}, 200)

@app.route('/user/<username>')
def param_route(username):
    return ({'message': f'Returning user with username: {username}'}, 200)

@app.route('/hello')
def hello():
    return ({'message': 'hello'}, 200)

@app.errorhandler(404)
def page_not_found(error):
    return ({'error': f'{error}'}, 404)
