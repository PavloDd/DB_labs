from flask import Flask


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .error_handler import err_handler_bp

    app.register_blueprint(err_handler_bp)

    from mydb.auth.route.music_label.album_route import album_bp
    from mydb.auth.route.music_label.author_route import author_bp
    from mydb.auth.route.music_label.genre_route import genre_bp
    from mydb.auth.route.music_label.music_label_route import music_label_bp
    from mydb.auth.route.music_label.playlist_has_user_route import playlist_has_user_bp
    from mydb.auth.route.music_label.playlist_route import playlist_bp
    from mydb.auth.route.music_label.song_has_playlists_route import (
        song_has_playlists_bp,
    )
    from mydb.auth.route.music_label.song_in_playlist_route import song_in_playlist_bp
    from mydb.auth.route.music_label.song_route import song_bp
    from mydb.auth.route.music_label.user_has_song_route import user_has_song_bp
    from mydb.auth.route.music_label.user_route import user_bp

    app.register_blueprint(album_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(music_label_bp)
    app.register_blueprint(playlist_has_user_bp)
    app.register_blueprint(playlist_bp)
    app.register_blueprint(song_has_playlists_bp)
    app.register_blueprint(song_in_playlist_bp)
    app.register_blueprint(song_bp)
    app.register_blueprint(user_has_song_bp)
    app.register_blueprint(user_bp)
