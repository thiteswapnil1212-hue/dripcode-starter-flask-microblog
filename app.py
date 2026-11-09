"""Flask Microblog — starter. Your logic goes here.
Steps: https://skill-grid-weld.vercel.app/projects/flask-microblog
"""

from flask import Flask, render_template

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    # TODO: show posts (newest first). For now, an empty list.
    return render_template("index.html", posts=[])


# TODO: User model (SQLAlchemy) + Post model.
# TODO: /register and /login routes (Flask-Login, hash passwords).
# TODO: /user/<username> profile page.
# TODO: /follow/<username> and /unfollow/<username>.
# TODO: new-post form on the index page (login required).

if __name__ == "__main__":
    app.run(debug=True)
