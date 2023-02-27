import logging
import os

from datetime import datetime, timedelta
from flask import jsonify, request
from sqlalchemy import and_
from random import randint

from config import app, db
from models import Token, User


port_number = int(os.environ.get("APP_PORT", 5151))


@app.route("/health_check")
def health_check():
    return "ok"


@app.route("/readiness_check")
def readiness_check():
    try:
        count = db.session.query(Token).count()
    except Exception as e:
        app.logger.error(e)
        return "failed", 500
    else:
        return "ok"


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
    app.run(host="0.0.0.0", port=port_number)
