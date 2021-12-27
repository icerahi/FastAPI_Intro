from pydantic import BaseModel

class ArticleSchema(BaseModel):
    title:str
    description:str 
    
    class Config:
        orm_mode=True

class MyArticleSchema(ArticleSchema):

    class Config:
        orm_mode=True
    