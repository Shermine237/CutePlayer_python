# Player UI
from PySide6.QtWidgets import QFileDialog, QDialog

from Packages.MultimediaDesignUI import MainWindows
from Packages.api.player import Player


class Windows(MainWindows):
    def __init__(self):
        super().__init__("Cute Player", (600, 600))
        # Players
        self.player = Player(self.video_widget)

        # Connect actions to slots
        self.open_action.triggered.connect(self.open_media)
        self.play_action.triggered.connect(self.player.play)
        self.pause_action.triggered.connect(self.player.pause)
        self.stop_action.triggered.connect(self.player.stop)
        self.prev_action.triggered.connect(self.player.prev)
        self.next_action.triggered.connect(self.player.next)

    # Methods

    # Slots
    def disable_buttons(self):
        state = self.player.PlaybackState
        if state == self.player.playing:
            self.play_action.setDisabled(True)
        elif state == self.player.paused:
            self.pause_action.setDisabled(True)
        elif state == self.player.stopped:
            self.stop_action.setDisabled(True)

    def open_media(self):
        file_dialog = QFileDialog(self)
        file_dialog.setMimeTypeFilters(["video/mp4"])
        response = file_dialog.exec_()
        if response == QDialog.Accepted:
            media = file_dialog.selectedFiles()[0]
            self.player.start_play_media(media)
