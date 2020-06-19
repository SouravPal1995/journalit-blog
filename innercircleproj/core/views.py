from flask import Blueprint, url_for, render_template, request
from innercircleproj.models import Post

core_blueprint = Blueprint('core', import_name = __name__)

@core_blueprint.route('/')
def home():
    page = request.args.get('page', 1)
    all_posts = Post.query.order_by(Post.date.desc()).paginate(page = int(page), per_page = 5)
    return render_template('home.html', all_posts = all_posts)

@core_blueprint.route('/about')
def about():
    return render_template('about.html')

