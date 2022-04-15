from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='True')
    rating = Column(Integer, server_default='0')
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))