from flask import Blueprint, render_template

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    return render_template('base.html')

@views_bp.route('/contacts')
def contacts():
    return render_template('contacts.html')

@views_bp.route('/resume')
def resume():
    return render_template('resume.html')
