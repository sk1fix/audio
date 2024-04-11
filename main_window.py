import sys
from main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import os


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.folderpath = None
        self.menu = None
        self.current_index = 0
        self.player = QMediaPlayer()
        self.ui.ope_folder.clicked.connect(self.select_folder)
        self.ui.left.clicked.connect(self.left_skip)
        self.ui.right.clicked.connect(self.right_skip)
        self.ui.pause.clicked.connect(self.pause_b)
        self.ui.loop.clicked.connect(self.repeat)
        self.time_slider = self.ui.time_line
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_slider)
        self.timer.start(1000)
        self.volume = self.ui.volume
        self.volume.setMinimum(0)
        self.volume.setMaximum(100)
        self.volume.setValue(50)
        self.player.setVolume(50)
        self.volume.setTickInterval(10)
        self.volume.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volume.valueChanged.connect(self.volume_ch)

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку')
        QtWidgets.QMessageBox.information(
            self, 'Папка выбрана', self.folderpath)
        self.files = os.listdir(self.folderpath)
        self.mp3_files = [file for file in self.files if file.endswith('.mp3')]

    def play_current(self):
        url = QUrl.fromLocalFile(
            self.folderpath+'/'+self.mp3_files[self.current_index])
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def left_skip(self):
        self.current_index = (self.current_index - 1) % len(self.mp3_files)
        self.play_current()

    def right_skip(self):
        self.current_index = (self.current_index + 1) % len(self.mp3_files)
        self.play_current()

    def pause_b(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def volume_ch(self):
        volume_ = self.volume.value()
        self.player.setVolume(volume_)

    def repeat(self):
        self.play_current()

    def volume_sound(self):
        pass

    def update_slider(self):
        current_value = self.time_slider.value()
        if current_value < self.time_slider.maximum():
            self.time_slider.setValue(current_value + 1)
        else:
            self.time_slider.setValue(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
