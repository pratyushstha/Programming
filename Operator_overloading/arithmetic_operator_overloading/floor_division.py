class Playlist : 
    def __init__(self, playlist_duration) : 
        self.playlist_duration = playlist_duration
    def __floordiv__(self, song_duration) : 
        return Playlist(self.playlist_duration//song_duration)
    def __str__(self) : 
        return f"The song can be played {self.playlist_duration} times during the Playlist duration"
p1 = Playlist(500)
print(p1//50)
