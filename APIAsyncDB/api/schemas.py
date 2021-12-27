from pydantic import BaseModel

class ArticleSchemaIn(BaseModel):
    title:str
    description:str
    