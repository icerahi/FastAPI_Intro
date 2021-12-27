from fastapi import FastAPI ,status,HTTPException
from typing import Optional,List
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_404_NOT_FOUND
from .schemas import ArticleSchema,MyArticleSchema
from .database import engine,SessionLocal 
from . import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#get 
@app.get('/articles/',response_model=List[MyArticleSchema])
def get_articles(db:Session=Depends(get_db)):
    articles = db.query(models.Article).all()
    return articles
  
#detailpath
@app.get('/articles/{id}',status_code=200,response_model=MyArticleSchema)
def article_details(id:int,db:Session=Depends(get_db)):
    #article = db.query(models.Article).filter(models.Article.id == id).first()
    article = db.query(models.Article).get(id)
    if article:
        return article
    raise HTTPException(status_code=404,detail='The article does not exists!!')


#create
@app.post('/articles/',status_code=status.HTTP_201_CREATED)
def add_article(article:ArticleSchema,db:Session=Depends(get_db)):
    new_article = models.Article(title=article.title,description=article.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

#update 
@app.put('/articles/{id}',status_code = status.HTTP_202_ACCEPTED)
def update_article(id,article:ArticleSchema,db:Session=Depends(get_db)):
    db.query(models.Article).filter(models.Article.id == id).update({'title':article.title,'description':article.description})
    db.commit()
    return {'message':'The data is updated!!'}

#delete 

@app.delete('/articles/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id:int,db:Session=Depends(get_db)):
    db.query(models.Article).filter(models.Article.id==id).delete(synchronize_session=False)
    db.commit()