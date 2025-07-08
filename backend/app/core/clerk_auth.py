from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
import requests

security = HTTPBearer()
CLERK_JWKS_URL = "https://<your-clerk-domain>/.well-known/jwks.json"

def get_current_user(token: str = Depends(security)):
    jwks = requests.get(CLERK_JWKS_URL).json()
    unverified_header = jwt.get_unverified_header(token.credentials)
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            public_key = jwt.construct_rsa_public_key(key)
            payload = jwt.decode(token.credentials, public_key, algorithms=[key["alg"]], audience="<your-clerk-audience>")
            return payload
    raise HTTPException(status_code=401, detail="Invalid JWT")
