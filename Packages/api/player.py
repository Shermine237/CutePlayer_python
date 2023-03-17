from PySide6.QtMultimedia import QMediaPlayer


class Player(QMediaPlayer):
    def __init__(self, output):
        super().__init__()
        self.setVideoOutput(output)  # Set output widget
        # Status media player
        self.playing = QMediaPlayer.PlaybackState.PlayingState
        self.paused = QMediaPlayer.PlaybackState.PausedState
        self.stopped = QMediaPlayer.PlaybackState.StoppedState

    # Methods
    def start_play_media(self, file_name):
        if file_name:
            self.setSource(file_name)
            self.play()

    def prev(self):     # 5 sec
        position = self.position() - 10000
        if position <= 0:
            position = 0
        self.setPosition(position)

    def next(self):     # 5 sec
        position = self.position() + 10000
        if position >= self.duration():
            position = self.duration()
        self.setPosition(position)
