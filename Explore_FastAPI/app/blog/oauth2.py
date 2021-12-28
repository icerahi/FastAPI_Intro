
from fastapi import Depends,HTTPException,status,security
from blog import token 
oauth2_scheme = security.OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(data:str=Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data,credentials_exception)
    