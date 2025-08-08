from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from database.models import ArticleData

def create_article(db:Session,request:ArticleBase):
    article = ArticleData(
        content = request.content,
        title = request.title,
        author_name = request.author_name,
        published=request.published,
        user_id= request.creator_id
        )
    db.add(article)
    db.commit()
    db.refresh()
    


# def get_article(db:Session,id:int):
#     article = db.query()