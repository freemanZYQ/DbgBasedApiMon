# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_debugger_config = QtWidgets.QWidget()
        self.tab_debugger_config.setObjectName("tab_debugger_config")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_debugger_config)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vlayout_debugger_config = QtWidgets.QVBoxLayout()
        self.vlayout_debugger_config.setObjectName("vlayout_debugger_config")
        self.scroll_debugger_config = QtWidgets.QScrollArea(self.tab_debugger_config)
        self.scroll_debugger_config.setWidgetResizable(True)
        self.scroll_debugger_config.setObjectName("scroll_debugger_config")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 725, 468))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_debugger_config.setWidget(self.scrollAreaWidgetContents)
        self.vlayout_debugger_config.addWidget(self.scroll_debugger_config)
        self.verticalLayout.addLayout(self.vlayout_debugger_config)
        self.tabWidget.addTab(self.tab_debugger_config, "")
        self.tab_api_global_config = QtWidgets.QWidget()
        self.tab_api_global_config.setObjectName("tab_api_global_config")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_api_global_config)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vlayout_api_global_config = QtWidgets.QVBoxLayout()
        self.vlayout_api_global_config.setObjectName("vlayout_api_global_config")
        self.scroll_api_global_config = QtWidgets.QScrollArea(self.tab_api_global_config)
        self.scroll_api_global_config.setWidgetResizable(True)
        self.scroll_api_global_config.setObjectName("scroll_api_global_config")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 725, 468))
        self.widget.setObjectName("widget")
        self.scroll_api_global_config.setWidget(self.widget)
        self.vlayout_api_global_config.addWidget(self.scroll_api_global_config)
        self.verticalLayout_2.addLayout(self.vlayout_api_global_config)
        self.tabWidget.addTab(self.tab_api_global_config, "")
        self.tab_api_select_config = QtWidgets.QWidget()
        self.tab_api_select_config.setObjectName("tab_api_select_config")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_api_select_config)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.vlayout_api_select_config = QtWidgets.QVBoxLayout()
        self.vlayout_api_select_config.setObjectName("vlayout_api_select_config")
        self.scroll_api_select_config = QtWidgets.QScrollArea(self.tab_api_select_config)
        self.scroll_api_select_config.setWidgetResizable(True)
        self.scroll_api_select_config.setObjectName("scroll_api_select_config")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 725, 468))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scroll_api_select_config.setWidget(self.scrollAreaWidgetContents_4)
        self.vlayout_api_select_config.addWidget(self.scroll_api_select_config)
        self.verticalLayout_6.addLayout(self.vlayout_api_select_config)
        self.tabWidget.addTab(self.tab_api_select_config, "")
        self.tab_api_config = QtWidgets.QWidget()
        self.tab_api_config.setObjectName("tab_api_config")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_api_config)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vlayout_api_config = QtWidgets.QVBoxLayout()
        self.vlayout_api_config.setObjectName("vlayout_api_config")
        self.scroll_api_config = QtWidgets.QScrollArea(self.tab_api_config)
        self.scroll_api_config.setWidgetResizable(True)
        self.scroll_api_config.setObjectName("scroll_api_config")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 725, 468))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_api_config.setWidget(self.scrollAreaWidgetContents_2)
        self.vlayout_api_config.addWidget(self.scroll_api_config)
        self.verticalLayout_4.addLayout(self.vlayout_api_config)
        self.tabWidget.addTab(self.tab_api_config, "")
        self.tab_debugee_config = QtWidgets.QWidget()
        self.tab_debugee_config.setObjectName("tab_debugee_config")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_debugee_config)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vlayout_debugee_config = QtWidgets.QVBoxLayout()
        self.vlayout_debugee_config.setObjectName("vlayout_debugee_config")
        self.scroll_debugee_config = QtWidgets.QScrollArea(self.tab_debugee_config)
        self.scroll_debugee_config.setWidgetResizable(True)
        self.scroll_debugee_config.setObjectName("scroll_debugee_config")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 725, 468))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scroll_debugee_config.setWidget(self.scrollAreaWidgetContents_3)
        self.vlayout_debugee_config.addWidget(self.scroll_debugee_config)
        self.verticalLayout_5.addLayout(self.vlayout_debugee_config)
        self.tabWidget.addTab(self.tab_debugee_config, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_OK = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_OK.setObjectName("btn_OK")
        self.horizontalLayout.addWidget(self.btn_OK)
        self.btn_Cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Cancel.setObjectName("btn_Cancel")
        self.horizontalLayout.addWidget(self.btn_Cancel)
        self.btn_Apply = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Apply.setObjectName("btn_Apply")
        self.horizontalLayout.addWidget(self.btn_Apply)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.splitter.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.btn_OK.clicked.connect(MainWindow.btn_OK_click)
        self.btn_Cancel.clicked.connect(MainWindow.btn_Cancel_clicked)
        self.btn_Apply.clicked.connect(MainWindow.btn_Apply_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debugger_config), _translate("MainWindow", "调试器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_api_global_config), _translate("MainWindow", "API监控 - 全局"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_api_select_config), _translate("MainWindow", "API监控 - 选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_api_config), _translate("MainWindow", "API监控 - API"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debugee_config), _translate("MainWindow", "模块监控"))
        self.btn_OK.setText(_translate("MainWindow", "确定"))
        self.btn_Cancel.setText(_translate("MainWindow", "取消"))
        self.btn_Apply.setText(_translate("MainWindow", "应用"))

