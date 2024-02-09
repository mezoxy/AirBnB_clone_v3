#!/usr/bin/python3
"""The module: index"""


from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


@app_views.route('/status')
def get_status():
    """returns a JSON: "status": 'OK'"""
    rep = {"status": "OK"}

    return jsonify(rep)


@app_views.route('/stats')
def nub_obj():
    """Create an endpoint that retrieves the number of each objects"""
    dictt = {}
    lista = {
            State: 'states',
            City: 'cities',
            User: 'users',
            Place: 'places',
            Review: 'reviews',
            Amenity: 'amenities'
            }

    for key, val in lista.items():
        count = storage.count(key)
        dictt[val] = count
    return jsonify(dictt)