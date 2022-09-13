from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from db import ENGINE, Base


# テーブル定義
class TestUserTable(Base):
    __tablename__ = "test_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    point = Column(Integer, nullable=False, default=0)


# モデル定義
class TestUser(BaseModel):
    id: int
    name: str
    point: int

    class Config:
        orm_mode = True


def main() -> None:
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
