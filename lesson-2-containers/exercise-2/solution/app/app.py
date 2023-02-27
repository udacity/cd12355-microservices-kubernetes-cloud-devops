import logging
import os
from datetime import datetime, timedelta
from random import randint

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "postgres")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    joined_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean)


class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=False, nullable=False)
    token = db.Column(db.String(6), index=True, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, index=False, unique=False, nullable=False, default=datetime.now())
    used_at = db.Column(db.DateTime, index=True, unique=False, nullable=True)


@app.route("/health_check")
def health_check():
    return "ok"


@app.route("/readiness_check")
def readiness_check():
    try:
        count = db.session.query(User).count()
    except Exception as e:
        app.logger.error(e)
        return "failed", 500
    else:
        return "ok"


@app.route("/api/users/<user_id>/tokens", methods=["POST"])
def generate_token(user_id: int):

    user = User.query.filter(User.id == user_id).first()
    if not user:
        return jsonify(
            {
                "message": f"User {user_id} was not found"
            }
        ), 404

    token = Token(
        user_id=user_id,
        token=str(randint(100000, 999999))  # Generate a random 6 digit number
    )

    db.session.add(token)
    db.session.commit()

    return jsonify(
        {
            "token": token.token
        }
    ), 200


@app.route("/api/tokens", methods=["POST"])
def validate_token():
    user_id = request.args.get("user_id")
    token_value = request.args.get("value")

    if not user_id and token_value:
        return jsonify(
            {
                "message": "user_id and token_value are required fields"
            }
        ), 400

    ten_minutes_ago = datetime.now() -  timedelta(minutes=10)

    token = Token.query.filter(
        and_(
            Token.user_id == user_id,
            Token.created_at >= ten_minutes_ago,
        )
    ).first()

    if token and token.used_at is None:
        # Mark the token as used
        token.used_at = datetime.now()
        db.session.commit()

        return jsonify(
            {
                "status": "Success"
            }
        ), 200
    else:
        return jsonify(
            {
                "message": "No valid token was found"
            }
        ), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151)
