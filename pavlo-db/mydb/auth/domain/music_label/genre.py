from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Genre(db.Model, IDto):
    __tablename__ = "genres"

    genreId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)

    songs = relationship("Song", back_populates="genre")

    def __repr__(self):
        return f"Genre(genreId={self.genreId}, name={self.name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Genre:
        return Genre(
            genreId=dto_dict.get("genreId"),
            name=dto_dict.get("name"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "genreId": self.genreId,
            "name": self.name,
        }
