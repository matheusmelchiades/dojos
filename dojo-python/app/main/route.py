from flask import Blueprint, render_template, abort

MainComponent = Blueprint('main', __name__)


@MainComponent.route('/')
def home():
    return {'status': 'RUNNNING'}
