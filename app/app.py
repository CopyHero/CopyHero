# coding:utf-8
from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()


# Dependency to verify the authorization token or API key
async def verify_token(
    authorization: str = Header(None), x_api_key: str = Header(None)
):
    if authorization:  # Check if 'Authorization' header is provided
        token = authorization.replace(
            "Bearer ", ""
        )  # Extract token from 'Bearer' scheme
    elif x_api_key:  # Check if 'x-api-key' header is provided
        token = x_api_key
    else:
        # Raise an HTTP 401 Unauthorized error if neither header is provided
        raise HTTPException(status_code=401, detail="Authorization token is missing")

    # Placeholder for actual user verification logic
    # user = QueryUser.query_by_api_key(token)
    # if not user:
    #    raise HTTPException(status_code=401, detail="Authorization token is missing")

    return {}  # Return an empty dictionary or user object


# Dependency to get user information after verifying the token
async def get_user_info(user: str = Depends(verify_token)):
    return user  # Return the user object or token information
