from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class PlaylistUserAssociation(db.Model, IDto):
    __tablename__ = "playlists_has_users"

    playlists_playlistID = Column(
        Integer, ForeignKey("playlists.playlistID"), primary_key=True
    )
    users_userID = Column(Integer, ForeignKey("users.userID"), primary_key=True)

    playlist = relationship("Playlist", back_populates="users")
    user = relationship("User", back_populates="playlists")

    def __repr__(self):
        return f"PlaylistUserAssociation(playlists_playlistID={self.playlists_playlistID}, users_userID={self.users_userID})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "PlaylistUserAssociation":
        return PlaylistUserAssociation(
            playlists_playlistID=dto_dict.get("playlists_playlistID"),
            users_userID=dto_dict.get("users_userID"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "playlists_playlistID": self.playlists_playlistID,
            "users_userID": self.users_userID,
        }
