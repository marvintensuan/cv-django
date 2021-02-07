import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .get_from_firestore import my_reddit_comments

bp = Blueprint('home', __name__)

@bp.route('/sample', methods=['GET'])
def home():
    context = my_reddit_comments()
    return render_template('sample.html', context=context)

@bp.route('/')
def baseee():
    return render_template('home.html')