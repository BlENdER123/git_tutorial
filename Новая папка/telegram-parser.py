#Tutorial https://www.youtube.com/watch?v=uvbM2mejVk8
 
# -*- coding: utf-8 -*-
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
# from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
#                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
# rom PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
#                          QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
#                         QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from asyncqt import QEventLoop
 
from importlib import reload
import telebot
import time
import logging
from bs4 import BeautifulSoup
import requests
from telebot import apihelper
from threading import Timer
 
logging.basicConfig(filename="logfile.py", level=logging.INFO)
 
list = ['https://t.me/SecLabNews/', 7728, 'https://t.me/overlamer1/', 621, 'https://t.me/thehackernews/', 717,
        'https://t.me/haccking/', 5006, 'https://t.me/opennet_ru/', 4377, 'https://t.me/dataleak/', 1693,
        'https://t.me/Social_engineering/', 1028, 'https://t.me/pystyle/', 110,
        'https://t.me/alexmakus/', 3489, 'https://t.me/xakep_ru/', 9200, 'https://t.me/webware/', 3062,
        'https://t.me/habr_com/', 44013, 'https://t.me/bookflow/', 1052,
        'https://t.me/thehaking/', 365, 'https://t.me/proglibrary/', 3925, 'https://t.me/python_lounge/', 284,
        'https://t.me/thecodemedia/', 2002, 'https://t.me/osintru/', 61, 'https://t.me/antichat/', 8426,
        'https://t.me/nuancesproghumor/', 751, 'https://t.me/howdyho_official/', 2334, 'https://t.me/gurupython', 188]
 
 
class Kanal:
    name: str = list[0]
    stpage: int = list[1]
    embaded: str = "?embed=1"
 
 
 
 
test2 = str(list)
 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(731, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 711, 181))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(250, 60, 451, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 60, 231, 21))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(390, 20, 311, 20))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 381, 21))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 120, 101, 31))
        self.CheckBox = QCheckBox(self.groupBox)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setGeometry(QRect(10, 90, 131, 17))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(220, 120, 201, 20))
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(220, 150, 201, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 120, 171, 21))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 150, 171, 21))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 430, 711, 151))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 271, 41))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 431, 21))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(450, 70, 251, 20))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 30, 401, 20))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 110, 101, 31))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 210, 711, 131))
        self.textBrowser = QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 691, 101))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 350, 711, 71))
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 30, 271, 21))
        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(280, 30, 171, 20))
        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(480, 20, 101, 31))
        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(600, 20, 91, 31))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 590, 91, 31))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(400, 590, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
 
        QMetaObject.connectSlotsByName(MainWindow)
 
    # setupUi
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"News collector", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow",
                                                          u"Main data",
                                                          None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"-108**********", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"ID Your chat id: -108**********",
                                                        None))
        self.lineEdit_3.setText(
            QCoreApplication.translate("MainWindow", u"11***********:AA***********", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"Your Telegram token: '11***********:AA***********'",
                                                        None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.CheckBox.setText(QCoreApplication.translate("MainWindow",
                                                         u"Use proxy",
                                                         None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"8.8.8.8", None))
        self.lineEdit_5.setDisabled(True)
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"8080", None))
        self.lineEdit_6.setDisabled(True)
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"IP address, example: https://8.8.8.8",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"Port, example: 8080",
                                                        None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"Add channel",
                                                            None))
        self.groupBox_2.setDisabled(True)
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"Channel lik: https://t.me/cnlname/",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"News number, only the last one will be resend: 9999",
                                                        None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Enter news number to add...", None))
        self.textBrowser.setText(QCoreApplication.translate("MainWindow", str(list), None))
        self.textBrowser.setDisabled(True)
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Enter link to add...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"List of entered channels",
                                                            None))
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow",
                                                            u"Delete channel",
                                                            None))
        self.groupBox_4.setDisabled(True)
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Enter chanel name: https://t.me/chlname/", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Enter chanel number...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delite", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Delite all", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_4.setDisabled(True)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Stop after next checking", None))
        self.pushButton_5.setDisabled(True)
    # retranslateUi
 
 
print(list)
listtt = []
 
 
def aph_reload(apihelper):
    apihelper = reload(apihelper)
 
 
class MainWindow(QMainWindow, Ui_MainWindow):
    global TOKEN
 
    def starter(self):
        listtt.clear()
        self.collector()
 
    def proxy(self):
        if self.CheckBox.isChecked() == True:
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
        if self.CheckBox.isChecked() == False:
            self.lineEdit_5.setEnabled(False)
            self.lineEdit_6.setEnabled(False)
 
    def delall(self):
        list.clear()
        self.textBrowser.clear()
        print(list)
 
    def add_chanel(self):
        print(list)
        showlist1 = str(list)
        self.textBrowser.setText(showlist1)
        try:
            req = requests.get(self.lineEdit.text() + self.lineEdit_2.text())
            chn_to_test = req.text
            soup = BeautifulSoup(chn_to_test, 'lxml')
            members = soup.find_all("meta", {"content": "https://telegram.org/img/t_logo.png"})
            if len(members) > 0:
                self.lineEdit.setText(
                    QCoreApplication.translate("MainWindow", u"Wrong channel or news number", None))
                self.lineEdit_2.setText(
                    QCoreApplication.translate("MainWindow", u"Wrong channel or news number", None))
            else:
                list.append(self.lineEdit.text())
                list.append(self.lineEdit_2.text())
                self.textBrowser.clear()
                showlist = str(list)
                self.textBrowser.setText(showlist)
        except Exception:
            self.lineEdit.setText(
                QCoreApplication.translate("MainWindow", u"Wrong channel or news number", None))
            self.lineEdit_2.setText(
                QCoreApplication.translate("MainWindow", u"Wrong channel or news number", None))
 
    def delete_chanel(self):
        delind = list.index(self.lineEdit_7.text())
        del list[delind]
        del list[delind]
        self.textBrowser.clear()
        showlist2 = str(list)
        self.textBrowser.setText(showlist2)
 
    def apply(self):
 
        aph_reload(apihelper)
        try:
            if self.CheckBox.isChecked() == False:
                bot = telebot.TeleBot(self.lineEdit_3.text())
                info = bot.get_me()
                if info != None:
                    print(f'Bot info: {info}')
                    chadi = self.lineEdit_4.text()
                    try:
                        bot.send_message(chat_id=chadi, text="Connection test")
                        print('No problem detected. Message send')
                        self.groupBox_2.setDisabled(False)
                        self.textBrowser.setDisabled(False)
                        self.pushButton_4.setDisabled(False)
                        self.groupBox_3.setDisabled(False)
                        self.groupBox_4.setDisabled(False)
                        self.pushButton_5.setDisabled(False)
                    except Exception:
                        self.lineEdit_4.setText(
                            QCoreApplication.translate("MainWindow", u"Wrong channel name!", None))
                        print("ConnectionError!!!")
            else:
                prxaddr = self.lineEdit_5.text()
                port = self.lineEdit_6.text()
                proxy_full = ("socks5://" + prxaddr + ":" + port)
                print(proxy_full)
                try:
                    apihelper.proxy = {'https': proxy_full}
                    apihelper.proxy = {'https': proxy_full}
                    bot = telebot.TeleBot(self.lineEdit_3.text())
                    info = bot.get_me()
                    print(info)
                    if info != None:
                        print(f'Bot info: {info}')
                        chadi = self.lineEdit_4.text()
                        try:
                            bot.send_message(chat_id=chadi, text="Connection test")
                            print('No problem detected. Message send')
                            self.groupBox_2.setDisabled(False)
                            self.textBrowser.setDisabled(False)
                            self.pushButton_4.setDisabled(False)
                            self.groupBox_3.setDisabled(False)
                            self.groupBox_4.setDisabled(False)
                            self.pushButton_5.setDisabled(False)
                        except Exception:
                            self.lineEdit_4.setText(
                                QCoreApplication.translate("MainWindow", u"Wrong channel name!", None))
                            print("ConnectionError!!!")
                except Exception:
                    print("Proxy error")
                    self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Proxy error", None))
                    self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Proxy error", None))
        except TypeError:
            self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Token error!", None))
            print("Error")
 
    def solver(self, link, counter2):
        print(link)
        print(list[counter2])
        bot = telebot.TeleBot(self.lineEdit_3.text())
        chadi = self.lineEdit_4.text()
 
        try:
            bot.send_message(chat_id=chadi, text=link)
            print('No problem detected. Message send')
        except OSError:
            print("ConnectionError - Sending again after 5 seconds!!!")
            time.sleep(5)
            bot.send_message(chat_id=chadi, text=link)
            print('Problem solved')
 
    def timer(self):
        print("timer on")
        t = Timer(500, self.collector)
        t.start()
        print("timer off")
 
    def collector(self):
        print("Collector started")
        self.groupBox.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.groupBox_4.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        counter = 0
        counter2 = 1
        Kanal.name = list[counter]
        Kanal.stpage = list[counter2]
        while True:
            print("Testing chanell", Kanal.name, Kanal.stpage)
            time.sleep(1)
            r = requests.get(Kanal.name + str(Kanal.stpage) + Kanal.embaded)
            data = r.text
            soup = BeautifulSoup(data, 'lxml')
            pg_not_fnd = soup.find_all("div", {"class": "tgme_widget_message_error"})
            if len(pg_not_fnd) > 0:
                print(list[counter2])
                print(Kanal.stpage)
 
                if int(list[counter2]) < int(Kanal.stpage):
                    list[counter2] = int(Kanal.stpage)
                    Kanal.stpage = str(int(Kanal.stpage) - 1)
                    print(Kanal.name + str(Kanal.stpage) + Kanal.embaded)
                    r1 = requests.get(Kanal.name + str(Kanal.stpage) + Kanal.embaded)
                    data1 = r1.text
                    soup1 = BeautifulSoup(data1, 'lxml')
                    for results in soup1.find_all("a", {"class": "tgme_widget_message_date"}):
                        link = results.get('href')
                        print(list[counter2])
 
                        self.solver(link, counter2)
                        print(list)
                counter = counter + 2
                counter2 = counter2 + 2
                stop = len(list)
                if counter >= stop:
                    print(list)
                    if len(listtt) == 0:
                        self.timer()
                        print("Sleeping1")
                    else:
                        aph_reload(apihelper)
                        print("api stoped")
                        self.groupBox.setEnabled(True)
                        self.groupBox_2.setEnabled(True)
                        self.groupBox_3.setEnabled(True)
                        self.groupBox_4.setEnabled(True)
                        self.pushButton_4.setEnabled(True)
                        self.pushButton_5.setEnabled(False)
 
                    print("stoper")
                    break
                Kanal.name = list[counter]
                Kanal.stpage = list[counter2]
            else:
                print(55)
                Kanal.stpage = str(int(Kanal.stpage) + 1)
 
                print(list[counter2])
    def stop(self):
        listtt.append(1)
        print("Stop pushed")
 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.apply)
        self.pushButton_3.clicked.connect(self.delete_chanel)
        self.pushButton_2.clicked.connect(self.add_chanel)
        self.pushButton_4.clicked.connect(self.starter)
        self.pushButton_5.clicked.connect(self.stop)
        self.pushButton_6.clicked.connect(self.delall)
        self.CheckBox.clicked.connect(self.proxy)
 
    async def start(self):
        self.show()
 
 
app = QApplication()
loop = QEventLoop(app)
window = MainWindow()
loop.create_task(window.start())
loop.run_forever()