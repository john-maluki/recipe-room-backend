# This file is responsible for signing , encoding , decoding and returning JWTS
import time
from typing import Dict
from datetime import datetime, timedelta

import jwt
from decouple import config

from ..models import User


JWT_SECRET = config("SECRET_KEY")
JWT_ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES")


def token_response(token: str):
    return {"access_token": token}


# function used for signing the JWT string
def signJWT(user: User) -> Dict[str, str]:
    user_data = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "profile_photo": user.profile_photo,
        "phone_number": user.phone_number,
        "country": user.country,
    }
    payload = {
        "sub": user_data,
        "expires": time.time() + (int(ACCESS_TOKEN_EXPIRE_MINUTES) * 60 * 12),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
