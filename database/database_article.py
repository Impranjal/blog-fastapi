from sqlalchemy.orm.session import Session
from schemas import ArticleRequestModel
from database.models import ArticleData
from exception import Storyexceptions
def create_article(db:Session,request:ArticleRequestModel):
    if request.content.startswith("Once upon a time"):
        raise Storyexceptions("No more stories over here")
    article = ArticleData(
        content = request.content,
        title = request.title,
        author_name = request.author_name,
        published=request.published,
        user_id= request.id
        )
    db.add(article)
    db.commit()
    db.refresh(article)
    
def get_all_article(db:Session):
    """
        Fetching the records of all the articles created
    """
    return db.query(ArticleData).all()

def get_article_by_id(db:Session,id:int):
    """
            Fetching the data of the articles added to the database by id
    """
    article_data_by_id = db.query(ArticleData).filter(ArticleData.id==id).first()
    return article_data_by_id

