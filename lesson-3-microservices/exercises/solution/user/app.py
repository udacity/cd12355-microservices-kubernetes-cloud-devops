import logging
import os

from datetime import datetime, timedelta
from flask import jsonify, request
from sqlalchemy import and_
from random import randint

from config import app, db
from models import Token, User


port_number = int(os.environ.get("APP_PORT", 5152))


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port_number)
