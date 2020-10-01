from flask import Blueprint
from flask import render_template, request, url_for, redirect, send_file
from modules import Comment
from extensions import db
from sending_email import send_email


main = Blueprint('main', __name__, template_folder='templates',
                 static_folder='static')


@main.route('/home', methods=['GET', 'POST'])
@main.route('/')
def home():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        comments = request.form.get("comments")
        if db.session.query(Comment).filter(Comment.username == username).count() == 0:
            data = Comment(username, email, comments)
            db.session.add(data)
            db.session.commit()
            send_email(username, email, comments)
        return render_template('main.html', message='You have submitted the message successfully!')
    return render_template('main.html')


# @main.route('/return-file/', methods=['GET'])
# def return_file():
    # return send_file('static\Software_developer_CV.pdf', attachment_filename='Software_developer_CV.pdf')


# @main.route('/create')
# def create():
    # db.create_all()
    # return 'All tables created!'
