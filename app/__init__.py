from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .lib.configuration import pg_uri, session_key, session_lifetime

app = Flask(__name__)

app.secret_key = session_key
app.permanent_session_lifetime = timedelta(minutes=session_lifetime)

app.config["SQLALCHEMY_DATABASE_URI"] = pg_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import *
from .routes import routes as blueprints

for blueprint, prefix in blueprints:
    if len(prefix):
        app.register_blueprint(blueprint, url_prefix=prefix)
        continue
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    # Run development server
    app.run(host="0.0.0.0", port=8000, debug=True)
