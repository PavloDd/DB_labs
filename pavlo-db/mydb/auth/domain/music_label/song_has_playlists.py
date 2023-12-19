from __future__ import annotations
from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class SongPlaylistAssociation(db.Model, IDto):
    __tablename__ = "songs_has_playlists"

    songs_songId = Column(Integer, ForeignKey("songs.songId"), primary_key=True)
    playlists_playlistID = Column(
        Integer, ForeignKey("playlists.playlistID"), primary_key=True
    )

    song = relationship("Song", back_populates="playlists")
    playlist = relationship("Playlist", back_populates="songs")

    def __repr__(self):
        return f"SongPlaylistAssociation(songs_songId={self.songs_songId}, playlists_playlistID={self.playlists_playlistID})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "SongPlaylistAssociation":
        return SongPlaylistAssociation(
            songs_songId=dto_dict.get("songs_songId"),
            playlists_playlistID=dto_dict.get("playlists_playlistID"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "songs_songId": self.songs_songId,
            "playlists_playlistID": self.playlists_playlistID,
        }
