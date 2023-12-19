from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Playlist(db.Model, IDto):
    __tablename__ = "playlists"

    playlistID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)

    users = relationship(
        "PlaylistUserAssociation",
        back_populates="playlist",
        primaryjoin="Playlist.playlistID == PlaylistUserAssociation.playlists_playlistID",
    )
    songs = relationship(
        "SongPlaylistAssociation",
        back_populates="playlist",
        primaryjoin="Playlist.playlistID == SongPlaylistAssociation.playlists_playlistID",
    )
    songs_in_playlist = relationship("SongInPlaylist", back_populates="playlist")

    def __repr__(self):
        return f"Playlist(playlistID={self.playlistID}, name={self.name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Playlist:
        return Playlist(
            playlistID=dto_dict.get("playlistID"),
            name=dto_dict.get("name"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "playlistID": self.playlistID,
            "name": self.name,
        }
