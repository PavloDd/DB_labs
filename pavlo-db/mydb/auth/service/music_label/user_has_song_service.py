from mydb.auth.dao import user_has_song_dao, user_dao, song_dao
from mydb.auth.service.general_service import GeneralService


class UserSongAssociationService(GeneralService):
    _dao = user_has_song_dao

    def user_song(self):
        user_has_songs = self._dao.find_all()
        result = {}

        for user_has_song in user_has_songs:
            song_id = user_has_song.users_userID
            if song_id not in result:
                song = song_dao.find_by_id(song_id)
                if song:
                    result[song_id] = {
                        song.name: [
                            user_dao.find_by_id(
                                obj.users_userID
                            ).put_into_dto()
                            for obj in song.users
                        ]
                    }

        return list(result.values())

    def song_user(self):
        user_has_songs = self._dao.find_all()
        result = {}

        for user_has_song in user_has_songs:
            user_id = user_has_song.songs_songId
            if user_id not in result:
                user = user_dao.find_by_id(user_id)
                if user:
                    result[user_id] = {
                        user.name: [
                            song_dao.find_by_id(
                                obj.songs_songId
                            ).put_into_dto()
                            for obj in user.songs
                        ]
                    }

        return list(result.values())
