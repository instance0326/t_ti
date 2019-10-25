from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2


class Ui_MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # 父類的構造函數

        self.timer_camera = QtCore.QTimer()  # 定義定時器，用於控制顯示視頻的幀率
        self.cap = cv2.VideoCapture()  # 視頻流
        self.CAM_NUM = 0  # 為0時表示視頻流來自筆記本內置攝像頭

        self.set_ui()  # 初始化程序界面
        self.slot_init()  # 初始化槽函數

    '''程序界面佈局'''

    def set_ui(self):
        self.__layout_main = QtWidgets.QHBoxLayout()  # 總佈局
        self.__layout_fun_button = QtWidgets.QVBoxLayout()  # 按鍵佈局
        self.__layout_data_show = QtWidgets.QVBoxLayout()  # 數據(視頻)顯示佈局
        self.button_open_camera = QtWidgets.QPushButton('打開相機') # 建立用於打開攝像頭的按鍵
        self.button_close = QtWidgets.QPushButton("退出") # 建立用於退出程序的按鍵
        self.button_open_camera.setMinimumHeight(50)  # 設置按鍵大小
        self.button_close.setMinimumHeight(50)

        self.button_close.move(10, 100)  # 移動按鍵
        '''信息顯示'''
        self.label_show_camera = QtWidgets.QLabel()  # 定義顯示視頻的Label
        self.label_show_camera.setFixedSize(641, 481)  # 給顯示視頻的Label設置大小為641x481
        '''把按鍵加入到按鍵佈局中'''
        self.__layout_fun_button.addWidget(self.button_open_camera)  # 把打開攝像頭的按鍵放到按鍵佈局中
        self.__layout_fun_button.addWidget(self.button_close)  # 把退出程序的按鍵放到按鍵佈局中
        '''把某些控件加入到總佈局中'''
        self.__layout_main.addLayout(self.__layout_fun_button)  # 把按鍵佈局加入到總佈局中
        self.__layout_main.addWidget(self.label_show_camera)  # 把用於顯示視頻的Label加入到總佈局中
        '''總佈局佈置好後就可以把總佈局作為參數傳入下面函數'''
        self.setLayout(self.__layout_main)  # 到這步才會顯示所有控件

    '''初始化所有槽函數'''

    def slot_init(self):
        self.button_open_camera.clicked.connect(
            self.button_open_camera_clicked)  # 若該按鍵被點擊，則調用button_open_camera_clicked()
        self.timer_camera.timeout.connect(self.show_camera)  # 若定時器結束，則調用show_camera()
        self.button_close.clicked.connect(self.close)  # 若該按鍵被點擊，則調用close()，注意這個close是父類QtWidgets.QWidget自帶的，會關閉程序

    '''槽函數之一'''

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定時器未啟動
            flag = self.cap.open(self.CAM_NUM)  # 參數是0，表示打開筆記本的內置攝像頭，參數是視頻文件路徑則打開視頻
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "請檢查相機於電腦是否連接正確", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30) # 定時器開始計時30ms，結果是每過30ms從攝像頭中取一幀顯示
                self.button_open_camera.setText('關閉相機')
        else:
            self.timer_camera.stop()  # 關閉定時器
            self.cap.release()  # 釋放視頻流
            self.label_show_camera.clear()  # 清空視頻顯示區域
            self.button_open_camera.setText('打開相機')

    def show_camera(self):
        flag, self.image = self.cap.read()  # 從視頻流中讀取

        show = cv2.resize(self.image, (640, 480))  # 把讀到的幀的大小重新設置為 640x480
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 視頻色彩轉換回RGB，這樣才是現實的顏色
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把讀取到的視頻數據變成QImage形式
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往顯示視頻的Label裡 顯示QImage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 固定的，表示程序應用
    ui = Ui_MainWindow()  # 實例化Ui_MainWindow
    ui.show()  # 調用ui的show()以顯示。同樣show()是源於父類QtWidgets.QWidget的
    sys.exit(app.exec_())  # 不加這句，程序界面會一閃而過
