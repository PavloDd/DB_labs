from mydb.auth.service.music_label.album_service import AlbumService
from mydb.auth.service.music_label.author_service import AuthorService
from mydb.auth.service.music_label.genre_service import GenreService
from mydb.auth.service.music_label.music_label_service import MusicLabelService
from mydb.auth.service.music_label.playlist_service import PlaylistService
from mydb.auth.service.music_label.playlist_has_user_service import (
    PlaylistUserAssociationService,
)
from mydb.auth.service.music_label.song_service import SongService
from mydb.auth.service.music_label.song_has_playlist_service import (
    SongPlaylistAssociationService,
)
from mydb.auth.service.music_label.song_in_playlist_service import SongInPlaylistService
from mydb.auth.service.music_label.user_service import UserService
from mydb.auth.service.music_label.user_has_song_service import (
    UserSongAssociationService,
)

album_service = AlbumService()
author_service = AuthorService()
genre_service = GenreService()
music_label_service = MusicLabelService()
playlist_service = PlaylistService()
playlist_has_user_service = PlaylistUserAssociationService()
song_service = SongService()
song_has_playlist_service = SongPlaylistAssociationService()
song_in_playlist_service = SongInPlaylistService()
user_service = UserService()
user_has_song_service = UserSongAssociationService()
