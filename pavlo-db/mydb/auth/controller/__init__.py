from mydb.auth.controller.music_label.album_controller import AlbumController
from mydb.auth.controller.music_label.author_controller import AuthorController
from mydb.auth.controller.music_label.genre_controller import GenreController
from mydb.auth.controller.music_label.music_label_controller import MusicLabelController
from mydb.auth.controller.music_label.playlist_controller import PlaylistController
from mydb.auth.controller.music_label.playlist_has_user_controller import (
    PlaylistUserAssociationController,
)
from mydb.auth.controller.music_label.song_controller import SongController
from mydb.auth.controller.music_label.song_has_playlist_controller import (
    SongPlaylistAssociationController,
)
from mydb.auth.controller.music_label.song_in_playlist_controller import (
    SongInPlaylistController,
)
from mydb.auth.controller.music_label.user_controller import UserController
from mydb.auth.controller.music_label.user_has_song_controller import (
    UserSongAssociationController,
)

album_controller = AlbumController()
author_controller = AuthorController()
genre_controller = GenreController()
music_label_controller = MusicLabelController()
playlist_controller = PlaylistController()
playlist_has_user_controller = PlaylistUserAssociationController()
song_controller = SongController()
song_has_playlist_controller = SongPlaylistAssociationController()
song_in_playlist_controller = SongInPlaylistController()
user_controller = UserController()
user_has_song_controller = UserSongAssociationController()
