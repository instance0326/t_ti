from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0

        self.set_ui()
        self.slot_init()

    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout()
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()
        self.button_open_camera = QtWidgets.QPushButton('打開相機')
        self.button_close = QtWidgets.QPushButton('退出')
        self.button_open_camera.setMinimumHeight(50)
        self.button_close.setMinimumHeight(50)
        self.button_close.move(10, 100)
        self.label_show_camera = QtWidgets.QLabel()
        self.label_show_camera.setFixedSize(641, 481)
        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)
        self.setLayout(self.__layout_main)

    def slot_init(self):
        self.button_open_camera.clicked.connect(
            self.button_open_camera_clicked)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)  # ???

    def button_open_camera_clicked(self):

        if self.timer_camera.isActive() == False:

            flag = self.cap.open(self.CAM_NUM)

            if flag == False:

                msg = QtWidgets.QMessageBox.warning(self, 'warning', "連接不成", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)
                self.button_open_camera.setText('關閉相機')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText('打開相機')

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
