from mydb.auth.dao import song_has_playlist_dao, playlist_dao, song_dao
from mydb.auth.service.general_service import GeneralService


class SongPlaylistAssociationService(GeneralService):
    _dao = song_has_playlist_dao

    def playlist_song(self):
        song_has_playlists = self._dao.find_all()
        result = {}

        for song_has_playlist in song_has_playlists:
            playlist_id = song_has_playlist.playlists_playlistID
            if playlist_id not in result:
                playlist = playlist_dao.find_by_id(playlist_id)
                result[playlist_id] = {
                    playlist.name: [
                        song_dao.find_by_id(
                            obj.songs_songId
                        ).put_into_dto()
                        for obj in playlist.songs
                    ]
                }

        return list(result.values())

    def song_playlist(self):
        song_has_playlists = self._dao.find_all()
        result = {}

        for song_has_playlist in song_has_playlists:
            song_id = song_has_playlist.playlists_playlistID
            if song_id not in result:
                song = song_dao.find_by_id(song_id)
                print(list(result.values()))
                result[song_id] = {
                    song.name: [
                        playlist_dao.find_by_id(
                            obj.songs_songId
                        ).put_into_dto()
                        for obj in song.playlists
                    ]
                }
        return list(result.values())
