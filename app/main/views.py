from flask import render_template,url_for,request,abort,redirect
from ..models import Blogpost,User,Comments
from .import main
from .forms import CommentForm,PostForm,UpdateProfile
from flask_login import login_required,current_user
from app import db
@main.route('/')
def index():
    '''a function to take a user to the home page'''
    posts=Blogpost.query.all()
    title="welcome to our new blog post"
    return render_template('index.html',title=title,posts=posts)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)
@main.route('/post',methods=['GET','POST'])
@login_required
def post():
    form=PostForm()
    if form.validate_on_submit():
        title=form.title.data
        content=form.content.data
        new_post=Blogpost(title=title,content=content)
        new_post.post_save()
        return redirect(url_for('main.index'))
    title='make a new blog here'
    return render_template('post.html',title=title,postform=form)
@main.route('/comment/<int:id>')
def view_comment(id):
    post=Blogpost.query.get(id)
    title='posts'
    return render_template('comment.html',title=title,post=post)
@main.route('/post/new_comment/<int:id>',methods=['GET','POST'])
def new_comment(id):
    post=Blogpost.query.get(id)
    form=CommentForm()
    if form.validate_on_submit():
        content=form.content.data
        new_comment=Comments(content=content,blogpost=post)
        new_comment.comment_save()
        return redirect(url_for('main.view_comment',id=post.id))
    title='make a new comment here'
    return render_template('new_comment.html',title=title,post=post,commentform=form)
@main.route('/post/comment/delete/<int:id>')
def delete_comment(id):
    post=Blogpost.query.get(id)
    return (post.title)
