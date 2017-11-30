#!flask/bin/python
import argparse, sys, os

from restserver import rest_server

reload(sys)
sys.setdefaultencoding('utf8')

here = os.path.dirname(os.path.realpath(__file__))

tasks = {}

parser=argparse.ArgumentParser(
    description='''Simple RESTful server ofr handling basic HTTP operations, serves as a todolist application. 
To test, simple run:\n
curl -i http://localhost:5000/todo/tasks\n
to test getting one element, run:\n
curl -i http://localhost:5000/todo/tasks/<id> ''',
    epilog="""""")
args=parser.parse_args()

def main(argv):
    rest_server(8080)

if __name__ == '__main__':
    main(sys.argv[1:])