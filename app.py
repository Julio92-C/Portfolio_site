from flask import Flask, Blueprint
from views import main
import extensions
from extensions import db


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '11eeo9_rCa0a@a#roCr/'

    ENV = 'prod'

    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:921016@localhost/portfolio'

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://voteexhtubnxyo:8b40c16582b032b3ead3351033cc957047ff7b70a56861a8c02d857629147136@ec2-3-228-114-251.compute-1.amazonaws.com:5432/d9f0l50lh8a8ai'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    extensions.bootstrap.init_app(app)

    app.register_blueprint(main)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app.run()
