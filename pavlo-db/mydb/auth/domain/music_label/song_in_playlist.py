from __future__ import annotations
from typing import Any

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class SongInPlaylist(db.Model, IDto):
    __tablename__ = "songs_in_playlist"

    song_in_playlist = Column(Integer, primary_key=True, autoincrement=True)
    in_order = Column(Enum("by ID", "by name", "random"))
    playlists_playlistID = Column(
        Integer, ForeignKey("playlists.playlistID"), nullable=False
    )

    playlist = relationship("Playlist", back_populates="songs_in_playlist")

    def __repr__(self):
        return f"SongInPlaylist(song_in_playlist={self.song_in_playlist}, in_order={self.in_order}, playlists_playlistID={self.playlists_playlistID})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> "SongInPlaylist":
        return SongInPlaylist(
            song_in_playlist=dto_dict.get("song_in_playlist"),
            in_order=dto_dict.get("in_order"),
            playlists_playlistID=dto_dict.get("playlists_playlistID"),
        )

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "song_in_playlist": self.song_in_playlist,
            "in_order": self.in_order,
            "playlists_playlistID": self.playlists_playlistID,
        }
