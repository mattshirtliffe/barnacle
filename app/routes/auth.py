

from flask import Blueprint, request, jsonify

# This instance of a Blueprint that represents the authentication blueprint
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/auth', methods=['POST'])
def login_user():
    bad_response = jsonify({
        'message': 'Invalid email or password, Please try again'
    })
    bad_response.status_code = 401

    post_data = request.get_json()
    try:
        email = post_data['email']
        password = post_data['password']
    except:
        return bad_response

    if email and password:
        user = User.query.filter_by(email=email).first()

    if not user:
        return bad_response
    else:

        if user.password_is_valid(password):
            response = jsonify({
                'message': 'You logged in successfully.',
                'token': user.generate_token()
            })
            response.status_code = 201
            return response

        else:
            return bad_response
