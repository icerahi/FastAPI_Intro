from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from blog.hashing import Hash

from blog import models,schemas

def create(request:schemas.User,db:Session):
    new_user = models.User(username=request.username,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail=f"user with this id {id} not found!!")
    
    return user