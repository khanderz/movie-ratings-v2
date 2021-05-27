"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from datetime import date



# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """return all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """return movie by id"""

    return Movie.query.get(movie_id)

def get_users():
    """return all users"""

    return User.query.all()


def get_user_by_id(user_id):
    """return user by id"""

    return User.query.get(user_id)

def create_rating(user, movie, score):
    """Create and return movie rating"""

    rating = Rating(user=user, score=score, movie=movie)

    db.session.add(rating)
    db.session.commit()

    return rating    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)