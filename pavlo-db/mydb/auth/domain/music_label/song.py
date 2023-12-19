from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Song(db.Model, IDto):
    __tablename__ = "songs"

    songId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    downloads = Column(String(45), nullable=False)
    albums_albumsID = Column(Integer, ForeignKey("albums.albumsID"), nullable=False)
    genres_genreId = Column(Integer, ForeignKey("genres.genreId"), nullable=False)
    authors_authorsID = Column(Integer, ForeignKey("authors.authorsID"), nullable=False)

    album = relationship("Album", back_populates="songs")
    genre = relationship("Genre", back_populates="songs")
    author = relationship("Author", back_populates="songs")
    playlists = relationship(
        "SongPlaylistAssociation",
        back_populates="song",
        primaryjoin="Song.songId == SongPlaylistAssociation.songs_songId",
    )
    users = relationship(
        "UserSongAssociation",
        back_populates="song",
        primaryjoin="Song.songId == UserSongAssociation.songs_songId",
    )

    def __repr__(self):
        return f"Song(songId={self.songId}, name={self.name}, price={self.price}, downloads={self.downloads})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "Song":
        return Song(
            songId=dto_dict.get("songId"),
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
            downloads=dto_dict.get("downloads"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "songId": self.songId,
            "name": self.name,
            "price": self.price,
            "downloads": self.downloads,
        }
