# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import logo

class Ui_Funy(QtWidgets.QWidget):
    def setupUi(self):
        self.resize(385, 315)
        self.setWindowTitle("Funy")
        self.setWindowIcon(QIcon(":/logo.svg"))
        self.setMinimumSize(QtCore.QSize(385, 315))
        self.setMaximumSize(QtCore.QSize(385, 315))
        self.setStyleSheet("background-color: #BDBDBD;")
        # let the window center
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int((screen.width() - window_size.width()) / 2),
                  int((screen.height() - window_size.height()) / 2))
        # ----------------------------------------------------------
        # sys tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(":/logo.svg"))
        showAction = QAction("打开", self, triggered = self.Show)
        quitAction = QAction("退出", self, triggered = QCoreApplication.instance().quit)
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(showAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()
        # -----------------------------------------------------------------
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.listWidget = QtWidgets.QListWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(90, 16777215))
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.listWidget.setStyleSheet("margin:10px 0px 10px 0px;")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(0)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        # ----------------------------
        item = self.listWidget.item(0)
        item.setText("彩虹屁")
        item = self.listWidget.item(1)
        item.setText("星座运势")
        item = self.listWidget.item(2)
        item.setText("天气查询")
        # ----------------------------
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setMidLineWidth(0)
        # ================================================
        self.page = QtWidgets.QWidget()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.textBrowser_chp = QtWidgets.QTextBrowser(self.page)
        self.verticalLayout.addWidget(self.textBrowser_chp)
        self.btn_next_chp = QtWidgets.QPushButton(self.page)
        self.btn_next_chp.setText("下一条")
        self.verticalLayout.addWidget(self.btn_next_chp)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.page)
        # ==========================================
        self.page_2 = QtWidgets.QWidget()
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.textBrowser_xz = QtWidgets.QTextBrowser(self.page_2)
        self.verticalLayout_3.addWidget(self.textBrowser_xz)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.input_xz = QtWidgets.QLineEdit(self.page_2)
        self.input_xz.setPlaceholderText("请输入星座的中文或者英文名字")
        self.input_xz.setToolTip("aries 白羊座, taurus 金牛座, gemini 双子座, \ncancer 巨蟹座, leo 狮子座, virgo 处女座, \nlibra 天秤座, scorpio 天蝎座, sagittarius 射手座, \ncapricorn 摩羯座, aquarius 水瓶座, pisces 双鱼座")
        self.horizontalLayout_3.addWidget(self.input_xz)
        self.btn_xz_search = QtWidgets.QPushButton("查询",self.page_2)
        self.horizontalLayout_3.addWidget(self.btn_xz_search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        # ===============================================
        self.page_3 = QtWidgets.QWidget()
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.textBrowser_weather = QtWidgets.QTextBrowser(self.page_3)
        self.verticalLayout_4.addWidget(self.textBrowser_weather)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.input_city = QtWidgets.QLineEdit(self.page_3)
        self.input_city.setPlaceholderText("请输入城市名字")
        self.input_city.setToolTip("北京，上海，新加坡等")
        self.horizontalLayout_4.addWidget(self.input_city)
        self.btn_weather_search = QtWidgets.QPushButton("查询",self.page_3)
        self.horizontalLayout_4.addWidget(self.btn_weather_search)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.page_3)
        # ===================================================
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.listWidget.setCurrentRow(0)  # 左侧选项栏
        self.stackedWidget.setCurrentIndex(0)  # 右侧多窗口
        QtCore.QMetaObject.connectSlotsByName(self)

    # 从系统托盘展示窗口
    def Show(self):
        self.showNormal()
        self.activateWindow()
        self.setWindowFlags(QtCore.Qt.Window)
        self.show()

     # 重写关闭事件
    def closeEvent(self, event):
        reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("确定要退出吗?"), QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
        else:
            event.ignore()
            # 最小化到托盘
            self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)