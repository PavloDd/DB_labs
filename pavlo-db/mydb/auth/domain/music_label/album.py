from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Album(db.Model, IDto):
    __tablename__ = "albums"

    albumsID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    authors_authorsID = Column(Integer, ForeignKey("authors.authorsID"), nullable=False)
    authors_music_labels_music_labelID = Column(Integer, nullable=False)

    author = relationship(
        "Author", back_populates="albums", foreign_keys=[authors_authorsID]
    )
    songs = relationship("Song", back_populates="album")

    def __repr__(self):
        return f"Album(albumsID={self.albumsID}, name={self.name}, year={self.year}, price={self.price}, authors_authorsID={self.authors_authorsID}, authors_music_labels_music_labelID={self.authors_music_labels_music_labelID})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Album:
        return Album(
            albumsID=dto_dict.get("albumsID"),
            name=dto_dict.get("name"),
            year=dto_dict.get("year"),
            price=dto_dict.get("price"),
            authors_authorsID=dto_dict.get("authors_authorsID"),
            authors_music_labels_music_labelID=dto_dict.get(
                "authors_music_labels_music_labelID"
            ),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "albumsID": self.albumsID,
            "name": self.name,
            "year": self.year,
            "price": self.price,
            "authors_authorsID": self.authors_authorsID,
            "authors_music_labels_music_labelID": self.authors_music_labels_music_labelID,
        }
