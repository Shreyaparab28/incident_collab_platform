# app/utils/auth.py

from jose import jwt
from jose.exceptions import JWTError
from fastapi import Request, HTTPException, status
from typing import Dict
import requests
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import base64

CLERK_JWKS_URL = "https://clear-sponge-52.clerk.accounts.dev/.well-known/jwks.json"
CLERK_ISSUER = "https://clear-sponge-52.clerk.accounts.dev"

jwks_cache = None

def get_jwks():
    global jwks_cache
    if jwks_cache is None:
        response = requests.get(CLERK_JWKS_URL)
        response.raise_for_status()
        jwks_cache = response.json()
    return jwks_cache

def get_current_user(request: Request) -> Dict:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header"
        )

    token = auth_header.split(" ")[1]
    jwks = get_jwks()

    try:
        header = jwt.get_unverified_header(token)
        key_data = next(
            (k for k in jwks["keys"] if k["kid"] == header["kid"]),
            None
        )
        if key_data is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Public key not found."
            )

        n = int.from_bytes(base64.urlsafe_b64decode(key_data["n"] + "=="), byteorder="big")
        e = int.from_bytes(base64.urlsafe_b64decode(key_data["e"] + "=="), byteorder="big")

        public_numbers = rsa.RSAPublicNumbers(e, n)
        public_key = public_numbers.public_key(default_backend())

        payload = jwt.decode(
            token,
            public_key,
            algorithms=[header["alg"]],
            issuer=CLERK_ISSUER
        )

        # DEBUG: Uncomment during testing to inspect Clerk JWT structure
        

        return {"user_id": payload.get("sub"), "username": payload.get("username") or payload.get("email") or payload.get("sub")
        }


    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token validation failed: {str(e)}"
        )
