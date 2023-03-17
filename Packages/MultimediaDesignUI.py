from PySide6.QtWidgets import QMainWindow, QToolBar, QStyle
from PySide6.QtMultimediaWidgets import QVideoWidget


class MainWindows(QMainWindow):
    def __init__(self, title, size):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(size[0], size[1])

        # Widgets
        self.video_widget = QVideoWidget()

        # Toolbar
        self.toolbar = QToolBar()

        # Menu
        self.file_menu = self.menuBar().addMenu("File")

        # Load Icons (load from Qt library) and save
        open_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogStart)
        play_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        pause_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
        stop_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop)
        prev_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekBackward)
        next_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekForward)

        # Add actions to menubar
        self.open_action = self.file_menu.addAction(open_icon, "Open")

        # Add actions to toolbar
        self.play_action = self.toolbar.addAction(play_icon, "Play")
        self.pause_action = self.toolbar.addAction(pause_icon, "Pause")
        self.stop_action = self.toolbar.addAction(stop_icon, "Stop")
        self.prev_action = self.toolbar.addAction(prev_icon, "Prev")
        self.next_action = self.toolbar.addAction(next_icon, "Next")

        # Add shortcuts
        self.open_action.setShortcut("Ctrl+O")

        # Add widgets to layout (QMainWindow already have layout, just add)
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.video_widget)  # central widget on QMainWindows
