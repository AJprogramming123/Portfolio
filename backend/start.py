from flask import Blueprint, render_template

start_bp = Blueprint('start', __name__)

@start_bp.route('/')
def start():
    return render_template('index.html')

@start_bp.route('/home')
def home():
    return render_template('home.html') 

@start_bp.route('/about')
def about():
    return render_template('stuff/about.html')

@start_bp.route('/projects')
def project():
    return render_template('stuff/project.html')

@start_bp.route('/socials')
def social():
    return render_template('stuff/social.html')