class Music:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print("Musiqa ijro etilmoqda")


class Song(Music):
    def __init__(self, title, artist, duration, genre):
        super().__init__(title, artist)
        self.duration = duration
        self.genre = genre

    def play(self):
        super().play()
        print(f"Nomi: {self.title}")
        print(f"Janr: {self.genre}")

    def stop(self):
        print("Musiqa to‘xtatildi")


s1 = Song("Believer", "Imagine Dragons", "3:20", "Rock")

s1.play()
s1.stop()
