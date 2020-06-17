from flask import Blueprint, url_for, render_template
from innercircleproj.models import Post

core_blueprint = Blueprint('core', import_name = __name__)

@core_blueprint.route('/')
def home():
    all_posts = Post.query.all()
    return render_template('home.html', all_posts = all_posts)

@core_blueprint.route('/about')
def about():
    return render_template('about.html')

