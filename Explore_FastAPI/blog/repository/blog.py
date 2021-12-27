
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from .. import models,schemas

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session,current_user:dict):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=current_user.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code =404,detail=f'blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail':'deleted successfull!!'}

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f'Blog with id {id} not found')
    
    # blog.update({'title':request.title,'body':request.body})
    blog.title=request.title
    blog.body = request.body
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(models.Blog).get(id)
    if not blog:
        raise HTTPException(status_code=404,detail="blog not found!!")
        # response.status_code =404
        # return {'detail':f'Blog with the id {id} not available!'}
    return blog