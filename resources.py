
from iot_models import practice1
from iot_db import session

from flask_restful import reqparse
from flask_restful import Resource
from flask_restful import abort
from flask_restful import fields
from flask_restful import marshal_with
from flask import request

import logging

iot_fields = {
    'sensorid': fields.String,
    'temperature': fields.String,
    'humidity': fields.String,
    'uri': fields.Url('iot', absolute=True),
}

class Sensor(Resource):
    @marshal_with(iot_fields)
    def put(self, sensorid, temperature, humidity):
        logging.info(request.headers.get('User-Agent'))
        iot = practice1(sensorid = sensorid, temperature = temperature, humidity = humidity)
        session.add(iot)
        session.commit()
        return iot, 201

