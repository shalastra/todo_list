#!flask/bin/python
import argparse

parser=argparse.ArgumentParser(
    description='''Simple RESTful server ofr handling basic HTTP operations, serves as a todolist application. 
To test, simple run:\n
curl -i http://localhost:5000/todo/tasks\n
to test getting one element, run:\n
curl -i http://localhost:5000/todo/tasks/<id> ''',
    epilog="""""")
args=parser.parse_args()