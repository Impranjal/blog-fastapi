from pydantic import BaseModel
from typing import Optional

class RequestModel(BaseModel):
    title : str
    id : int
    content : str
    author_name :str
    published : Optional[bool]
