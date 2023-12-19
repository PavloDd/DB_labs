from mydb.auth.dao.music_label.album_dao import AlbumDao
from mydb.auth.dao.music_label.author_dao import AuthorDao
from mydb.auth.dao.music_label.genre_dao import GenreDao
from mydb.auth.dao.music_label.music_label_dao import MusicLabelDao
from mydb.auth.dao.music_label.playlist_dao import PlaylistDao
from mydb.auth.dao.music_label.playlist_has_user_dao import PlaylistUserAssociationDao
from mydb.auth.dao.music_label.song_dao import SongDao
from mydb.auth.dao.music_label.song_has_playlist_dao import SongPlaylistAssociationDao
from mydb.auth.dao.music_label.song_in_playlist_dao import SongInPlaylistDao
from mydb.auth.dao.music_label.user_dao import UserDao
from mydb.auth.dao.music_label.user_has_song_dao import UserSongAssociationDao

album_dao = AlbumDao()
author_dao = AuthorDao()
genre_dao = GenreDao()
music_label_dao = MusicLabelDao()
playlist_dao = PlaylistDao()
playlist_has_user_dao = PlaylistUserAssociationDao()
song_dao = SongDao()
song_has_playlist_dao = SongPlaylistAssociationDao()
song_in_playlist_dao = SongInPlaylistDao()
user_dao = UserDao()
user_has_song_dao = UserSongAssociationDao()
