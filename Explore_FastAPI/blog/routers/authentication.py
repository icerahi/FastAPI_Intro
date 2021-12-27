from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from datetime import timedelta
from .. import schemas,database,models,token
from ..hashing import Hash

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail="Incorrect Password!!")

    # generat a jwt token 
    
    access_token = token.create_access_token(
        data={"sub": user.email,'user_id':user.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
   