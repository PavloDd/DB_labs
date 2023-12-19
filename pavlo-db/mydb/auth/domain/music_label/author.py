from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto
from mydb.auth.domain.music_label.album import Album


class Author(db.Model, IDto):
    __tablename__ = "authors"

    authorsID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)
    music_labels_music_labelID = Column(
        Integer, ForeignKey("music_labels.music_labelID"), nullable=False
    )

    music_label = relationship(
        "MusicLabel",
        back_populates="authors",
        foreign_keys=[music_labels_music_labelID],
    )
    albums = relationship("Album", back_populates="author")
    songs = relationship("Song", back_populates="author")

    def __repr__(self):
        return f"Author(authorsID={self.authorsID}, name={self.name}, music_labels_music_labelID={self.music_labels_music_labelID})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "Author":
        return Author(
            authorsID=dto_dict.get("authorsID"),
            name=dto_dict.get("name"),
            music_labels_music_labelID=dto_dict.get("music_labels_music_labelID"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "authorsID": self.authorsID,
            "name": self.name,
            "music_labels_music_labelID": self.music_labels_music_labelID,
        }
