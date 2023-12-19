from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class MusicLabel(db.Model, IDto):
    __tablename__ = "music_labels"

    music_labelID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)

    authors = relationship("Author", back_populates="music_label")

    def __repr__(self):
        return f"MusicLabel(music_labelID={self.music_labelID}, name={self.name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "MusicLabel":
        return MusicLabel(
            music_labelID=dto_dict.get("music_labelID"),
            name=dto_dict.get("name"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "music_labelID": self.music_labelID,
            "name": self.name,
        }
