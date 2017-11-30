#!flask/bin/python
import argparse, sys, os

from restserver import rest_server

reload(sys)
sys.setdefaultencoding('utf8')

here = os.path.dirname(os.path.realpath(__file__))

tasks = {}

with open('help.txt') as f:
    content = f.readlines()

parser=argparse.ArgumentParser(
    usage=''.join(content),
    epilog="""""")
args=parser.parse_args()

def main(argv):
    rest_server(8080)

if __name__ == '__main__':
    main(sys.argv[1:])