from mydb.auth.dao import playlist_has_user_dao, user_dao, playlist_dao
from mydb.auth.service.general_service import GeneralService


class PlaylistUserAssociationService(GeneralService):
    _dao = playlist_has_user_dao

    def playlist_user(self):
        playlist_has_users = self._dao.find_all()
        result = {}

        for playlist_has_user in playlist_has_users:
            user_id = playlist_has_user.users_userID
            if user_id not in result:
                user = user_dao.find_by_id(user_id)
                result[user_id] = {
                    user.name: [
                        playlist_dao.find_by_id(
                            obj.playlists_playlistID
                        ).put_into_dto()
                        for obj in user.playlists
                    ]
                }

        return list(result.values())

    def user_playlist(self):
        playlist_has_users = self._dao.find_all()
        result = {}

        for playlist_has_user in playlist_has_users:
            playlist_id = playlist_has_user.playlists_playlistID
            if playlist_id not in result:
                playlist = playlist_dao.find_by_id(playlist_id)
                result[playlist_id] = {
                    playlist.name: [
                        playlist_dao.find_by_id(
                            obj.users_userID
                        ).put_into_dto()
                        for obj in playlist.users
                    ]
                }

        return list(result.values())
