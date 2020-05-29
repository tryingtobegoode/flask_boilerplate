import os

from flask import abort, Flask, jsonify, request
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity)
from flask_jwt_extended import JWTManager 

import requests



app = Flask(__name__)

##### EMPTY
###
##
#
@app.route('/', methods = ['POST'])
def empty():

    message = { 
        "name":"name"
    }

    return jsonify( message )