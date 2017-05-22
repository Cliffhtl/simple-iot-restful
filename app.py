#!/usr/bin/python

# Author: Orozco Hsu
# Date: 2017-05-13
# Org: DataService IoT training class sample

import logging

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import Sensor

api.add_resource(Sensor, '/iot/<string:sensorid>/<string:temperature>/<string:humidity>', endpoint='iot')


def main():
    logging.basicConfig(filename='iot.log', level=logging.INFO)
    try:
        logging.info('Started ltu lot api...')
        app.run(debug=True,host='172.104.90.53',port=5001)
    except Exception as ex:
        logging.error(ex)

if __name__ == '__main__':
    main()
