from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import Response
from ..database import SessionLocal
from .. import schemas,database,models,oauth2
from typing import List
from .. import models
from ..repository import blog

router = APIRouter(prefix='/blog',tags=['blogs']) 


get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=201)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    # new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    
    return blog.create(request,db,current_user)

        
# @router.get('/',status_code=200,response_model=List[schemas.ShowBlog])
# def all(db:Session=Depends(get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
#     # blogs = db.query(models.Blog).all()
#     # return blogs
#     return blog.get_all(db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)


@router.delete('/{id}',status_code=204) #
def destroy(id:int,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destory(id,db)

@router.put('/{id}',status_code=202)
def update(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)