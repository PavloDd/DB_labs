from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)

    playlists = relationship(
        "PlaylistUserAssociation",
        back_populates="user",
        primaryjoin="User.userID == PlaylistUserAssociation.users_userID",
    )
    songs = relationship(
        "UserSongAssociation",
        back_populates="user",
        primaryjoin="User.userID == UserSongAssociation.users_userID",
    )

    def __repr__(self):
        return f"User(id=0, name={self.name}, email={self.email})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        return User(
            userID=dto_dict.get("userID"),
            name=dto_dict.get("name"),
            email=dto_dict.get("email"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
        }
