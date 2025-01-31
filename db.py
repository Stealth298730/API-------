from sqlalchemy import String,create_engine
from sqlalchemy.orm import sessionmaker,Mapped ,mapped_column ,DeclarativeBase
engine = create_engine("sqlite:///tables.db" ,echo = True) 
Session = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass


class Table(Base):
    __tablename__ = "tables"

    id:Mapped[int] = mapped_column(primary_key=True)
    author:Mapped[str] = mapped_column (String(100))
    text:Mapped[str] = mapped_column (String())

def create_db():
    Base.metadata.create_all(bind=engine)

