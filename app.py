#!/usr/bin/env python

from flask import Flask, abort, request
import logging
import argparse

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", dest="logLevel", choices=[
                    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 
                    default='INFO',
                    help="Set the logging level")

args = parser.parse_args()
if args.logLevel:
    logging.basicConfig(level=getattr(logging, args.logLevel),
                        format='%(asctime)s | %(levelname)s: %(message)s')


@app.route('/', methods=['GET', 'POST'])
def api_endpoint():
    logging.debug("Received request - {}".format(request.url))
    if "application/json" in request.headers.getlist('accept'):
        return '{"message": "Good morning"}'
    return "<p>Hello, World</p>"

if __name__ == '__main__':
    try:
        logging.debug("Starting Flask server")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
	    logging.debug("Flask failed to start - Error: {}".format(e))

