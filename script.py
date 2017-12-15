#! /usr/bin/env python

import argparse
import os
import sys

from restserver import rest_server

reload(sys)
sys.setdefaultencoding('utf8')

# gets absolute path to scripts directory
path= os.path.dirname(os.path.abspath(__file__))
# opens help.txt file where help text is stored, accessed by -h or --help
with open(path+'/help.txt') as f:
    content = f.readlines()

parser = argparse.ArgumentParser(
    usage=''.join(content),
    epilog="""""")
args = parser.parse_args()

# initialize REST server on 8080 port
def main(argv):
    rest_server(8080)


if __name__ == '__main__':
    main(sys.argv[1:])
