from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData,
    Table,
    create_engine
)
from databases import Database

DATABASE_URL = "mysql://root:@127.0.0.1/articledb"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

i = 0
def mydefault():
    global i
    i += 1
    return i

Article = Table(
    "article",
    metadata,
    Column("id", Integer,primary_key=True),
    Column("title", String(100)),
    Column("description", String(500)),
                )

database = Database(DATABASE_URL)