from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from blog.hashing import Hash
from blog import database,models,schemas
from blog.repository import user

router=APIRouter(prefix='/user',tags=['users'])
get_db = database.get_db


@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.show(id,db)