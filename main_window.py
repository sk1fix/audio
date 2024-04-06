import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.folderpath = None
        self.menu = None
        self.label = QtWidgets.QLabel("Выберите папку с аудиофайлами")
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку")
        self.select_folder_button.clicked.connect(self.select_folder)


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Выберите папку')
        QtWidgets.QMessageBox.information(
            self, 'Папка выбрана', self.folderpath)
        if self.folderpath:
            self.menu = subWindow(self)
            self.menu.show()


class subWindow(QtWidgets.QDialog):
    def __init__(self, Main: Window = None) -> None:
        super(subWindow, self).__init__(Main)
        self.setModal(True)
        self.main_window = Main
        if Main is not None:
            self.Main = Main

        layout = QtWidgets.QVBoxLayout()

        self.button_left = QtWidgets.QPushButton("Назад")
        self.button_left.clicked.connect(self.left_skip)
        layout.addWidget(self.button_left)

        self.button_right = QtWidgets.QPushButton("Вперед")
        self.button_right.clicked.connect(self.pause)
        layout.addWidget(self.button_right)

        self.button_pause = QtWidgets.QPushButton("Пауза")
        self.button_pause.clicked.connect(self.pause)
        layout.addWidget(self.button_pause) 

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)  
        self.slider.setTickInterval(10)  
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)  
        layout.addWidget(self.slider)

        self.slider_time = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_time.setRange(0, 100)  
        layout.addWidget(self.slider_time)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_slider)
        self.timer.start(1000)  
        self.setLayout(layout)

        self.button_repeat = QtWidgets.QPushButton("Повторить")
        self.button_repeat.clicked.connect(self.repeat)
        layout.addWidget(self.button_repeat)

        self.setLayout(layout)
    def left_skip(self):
        pass

    def right_skip(self):
        pass

    def pause(self):
        pass  
    
    def volume(self):
        pass
    
    def repeat(self):
        pass
    
    def update_slider(self):
        current_value = self.slider_time.value()
        if current_value < self.slider_time.maximum():
            self.slider_time.setValue(current_value + 1)
        else:
            self.slider_time.setValue(0)  
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())