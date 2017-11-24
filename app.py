#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

import argparse

parser=argparse.ArgumentParser(
    description='''Simple RESTful server ofr handling basic HTTP operations, serves as a todolist application. 
To test, simple run:\n
curl -i http://localhost:5000/todo/tasks\n
to test getting one element, run:\n
curl -i http://localhost:5000/todo/tasks/<id> ''',
    epilog="""""")
args=parser.parse_args()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
