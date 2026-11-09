# Flask Microblog — DripCode Starter

Build a microblogging app with Python and Flask. This is the starter code
for the [DripCode Build Projects](https://skill-grid-weld.vercel.app/projects/flask-microblog) Flask Microblog project.

## What you will build

- User signup + login (passwords hashed, never plain text)
- Posts, profile pages, follow / unfollow, a feed of followed users

## Run it

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

Then open http://127.0.0.1:5000.

## Files

- `app.py` — the Flask app (routes are stubs — `TODO` marks the spots)
- `config.py` — settings (secret key, database)
- `requirements.txt` — Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF
- `templates/` — Jinja templates (base + index)

## Steps

Follow the steps on the [project page](https://skill-grid-weld.vercel.app/projects/flask-microblog). Tutorial: Miguel Grinberg's Flask Mega-Tutorial.

No solution code is included — you write it.
