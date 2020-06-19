from flask import Blueprint, render_template, redirect, flash, url_for
from innercircleproj.blogposts.forms import PostForm, PostEditForm
from innercircleproj.models import Post
from innercircleproj import db#, login_manager
from flask_login import current_user, login_required
import datetime as dt

post_bp = Blueprint("post", __name__)

@post_bp.route('/post/new', methods = ['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        bpost = Post(title, post, current_user.id)
        db.session.add(bpost)
        db.session.commit()
        flash("New Post Added!!")
        return redirect(url_for('core.home'))
    return render_template('post.html', form = form)

@post_bp.route('/post/<int:post_id>')
@login_required
def view_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post_details.html', post = post)

@post_bp.route('/post/<int:post_id>/edit', methods = ['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get(post_id)
    form = PostEditForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.post.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('post.view_post', post_id =post.id))
    else:
        form.title.data = post.title
        form.post.data = post.text
    return render_template('edit_post.html', form = form)

@post_bp.route('/post/<int:post_id>/delete')
def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f'{post.title} has been deleted!!')
    return redirect(url_for('core.home'))


