from typing import List
from fastapi import FastAPI,Depends,HTTPException,Response

from .hashing import Hash
from .schemas import Blog,ShowBlog, ShowUser, User
from . import models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from . import database
from .routers import blog,user,authentication

models.Base.metadata.create_all(engine)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

get_db = database.get_db

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# @app.post('/blog',status_code=201,tags=['blogs'])
# def create(request:Blog,db:Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',status_code=200,response_model=List[ShowBlog],tags=['blogs'])
# def all(db:Session=Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200,response_model=ShowBlog,tags=['blogs'])
# def show(id:int,response:Response,db:Session=Depends(get_db)):
#     blog = db.query(models.Blog).get(id)
#     if not blog:
#         raise HTTPException(status_code=404,detail="blog not found!!")
#         # response.status_code =404
#         # return {'detail':f'Blog with the id {id} not available!'}
#     return blog


# @app.delete('/blog/{id}',status_code=204,tags=['blogs']) #
# def destroy(id:int,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code =404,detail=f'blog with id {id} not found')
    
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {'detail':'deleted successfull!!'}

# @app.put('/blog/{id}',status_code=202,tags=['blogs'])
# def update(id:int,request:Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=404,detail=f'Blog with id {id} not found')
    
#     # blog.update({'title':request.title,'body':request.body})
#     blog.title=request.title
#     blog.body = request.body
#     db.commit()
#     return 'updated'


# @app.post('/user',response_model=ShowUser,tags=['users'])
# def create_user(request:User,db:Session=Depends(get_db)):
#     new_user = models.User(username=request.username,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=ShowUser,tags=['users'])
# def get_user(id:int,db:Session=Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#         raise HTTPException(status_code=404,detail=f"user with this id {id} not found!!")
    
#     return user