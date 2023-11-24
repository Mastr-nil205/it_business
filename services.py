import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('services', __name__, url_prefix='/services')

@bp.route('/itservices', methods=['GET'])
def itservices():
    """
    A route decorator that handles the '/itservices' endpoint.
    It renders the 'itservices.html' template.
    """
    if request.method == 'GET':
        return render_template('services/itservices.html')

@bp.route('/cloudservices')
def cloudservices():
    """
    Route decorator for the '/cloudservices' endpoint.
    This function renders the 'cloudservices.html' template.
    """
    return render_template('services/cloudservices.html')

