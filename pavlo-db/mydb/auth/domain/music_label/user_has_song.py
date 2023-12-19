from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class UserSongAssociation(db.Model, IDto):
    __tablename__ = "users_has_songs"

    users_userID = Column(Integer, ForeignKey("users.userID"), primary_key=True)
    songs_songId = Column(Integer, ForeignKey("songs.songId"), primary_key=True)

    user = relationship("User", back_populates="songs")
    song = relationship("Song", back_populates="users")

    def __repr__(self):
        return f"UserSongAssociation(users_userID={self.users_userID}, songs_songId={self.songs_songId})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "UserSongAssociation":
        return UserSongAssociation(
            users_userID=dto_dict.get("users_userID"),
            songs_songId=dto_dict.get("songs_songId"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "users_userID": self.users_userID,
            "songs_songId": self.songs_songId,
        }
