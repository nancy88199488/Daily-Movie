from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review

# Views
@main.route('/')
def index():
    movies = Movie.query.all()
    action = Movie.query.filter_by(category = "action").all()
    comedy = Movie.query.filter_by(category = "comedy").all() 
    drama = Movie.query.filter_by(category = "drama").all()
    horror = Movie.query.filter_by(category = "horror").all()
    return render_template('index.html', action=action, comedy=comedy ,drama=drama,horror=horror)

@main.route('/create_new', methods=['POST', 'GET'])
@login_required
def new_movie():
    form = MovieForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_movie_object = Movie(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_movie_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_movie.html', form = form)