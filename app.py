from flask import render_template
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bye")
def bye():
    return """
                <label for="pass">Password</label>
                <input type="password" id="pass">
            """


@app.route("/hello/<username>")
def hello_user(username):
    return render_template('hello_user.html', username=username)


@app.route('/login')
def login():
    return 'login'


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))



@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('show_post.html', post_id=post_id)