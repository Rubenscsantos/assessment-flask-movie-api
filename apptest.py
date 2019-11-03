import os
import tempfile

import pytest

from flaskr import flaskr

from flask import request, jsonify

@app.route('/')
def test_health_check():
    json_data = request.get_json()
    print(json_data)
    # return jsonify(token=generate_token(email, password))