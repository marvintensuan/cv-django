import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from google.cloud import firestore

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET'])
def home():

    context = my_reddit_comments()

    return render_template('sample.html', context=context)

def my_reddit_comments():
    db = firestore.Client()
    coll = db.collection('tagapagtuos_submissions').stream()
    db = None

    return [doc.to_dict() for doc in coll]

@bp.route('/cv')
def baseee():
    return render_template('home.html')