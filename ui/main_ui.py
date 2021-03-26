# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainptydyL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(495, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.header)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 0)
        self.label_9 = QLabel(self.header)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.header)

        self.body = QTabWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.TM = QWidget()
        self.TM.setObjectName(u"TM")
        self.verticalLayout_2 = QVBoxLayout(self.TM)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.TM)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(135, 0))

        self.horizontalLayout.addWidget(self.label)

        self.fromApiKey = QLineEdit(self.frame)
        self.fromApiKey.setObjectName(u"fromApiKey")
        self.fromApiKey.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.fromApiKey)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.TM)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.toApiKey = QLineEdit(self.frame_2)
        self.toApiKey.setObjectName(u"toApiKey")
        self.toApiKey.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.toApiKey)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.TM)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.rubbleSum = QLineEdit(self.frame_3)
        self.rubbleSum.setObjectName(u"rubbleSum")

        self.horizontalLayout_3.addWidget(self.rubbleSum)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.copSum = QLineEdit(self.frame_3)
        self.copSum.setObjectName(u"copSum")

        self.horizontalLayout_3.addWidget(self.copSum)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.TM)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"text-decoration: underline;\n"
"color: rgb(0, 0, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.paymentPassword = QLineEdit(self.frame_5)
        self.paymentPassword.setObjectName(u"paymentPassword")
        self.paymentPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.paymentPassword)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.PaymentLinkLabel = QLabel(self.frame_4)
        self.PaymentLinkLabel.setObjectName(u"PaymentLinkLabel")
        self.PaymentLinkLabel.setMaximumSize(QSize(16777215, 20))
        self.PaymentLinkLabel.setAlignment(Qt.AlignCenter)
        self.PaymentLinkLabel.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.PaymentLinkLabel)

        self.sendButton = QPushButton(self.frame_4)
        self.sendButton.setObjectName(u"sendButton")

        self.verticalLayout_3.addWidget(self.sendButton)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.body.addTab(self.TM, "")
        self.waxPage = QWidget()
        self.waxPage.setObjectName(u"waxPage")
        self.verticalLayout_4 = QVBoxLayout(self.waxPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.waxPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.fromWaxKey = QLineEdit(self.frame_6)
        self.fromWaxKey.setObjectName(u"fromWaxKey")
        self.fromWaxKey.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.fromWaxKey)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.waxPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(135, 0))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.steamId = QLineEdit(self.frame_7)
        self.steamId.setObjectName(u"steamId")
        self.steamId.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_8.addWidget(self.steamId)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.waxPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.dollarSum = QLineEdit(self.frame_10)
        self.dollarSum.setObjectName(u"dollarSum")

        self.horizontalLayout_9.addWidget(self.dollarSum)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.centSum = QLineEdit(self.frame_10)
        self.centSum.setObjectName(u"centSum")

        self.horizontalLayout_9.addWidget(self.centSum)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 30))
        self.label_12.setStyleSheet(u"text-decoration: underline;\n"
"color: rgb(0, 0, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_12)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.sendButton_2 = QPushButton(self.waxPage)
        self.sendButton_2.setObjectName(u"sendButton_2")

        self.verticalLayout_4.addWidget(self.sendButton_2)

        self.body.addTab(self.waxPage, "")

        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 30))
        self.footer.setMaximumSize(QSize(16777215, 30))
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 0, 6, 0)
        self.versionLabel = QLabel(self.footer)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout_5.addWidget(self.versionLabel)

        self.creditLabel = QLabel(self.footer)
        self.creditLabel.setObjectName(u"creditLabel")
        self.creditLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.creditLabel.setOpenExternalLinks(True)

        self.horizontalLayout_5.addWidget(self.creditLabel)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.body.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0410\u0432\u0442\u043e\u0440 \u043d\u0435 \u043d\u0435\u0441\u0435\u0442 \u043d\u0438\u043a\u0430\u043a\u043e\u0439 \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u0438 \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043d\u0435\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445</p><p>\u0438 \u043f\u0440\u043e\u0447\u0438\u0445 \u043e\u0448\u0438\u0431\u043e\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"API-KEY \u043e\u0442\u043a\u0443\u0434\u0430 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u043c", None))
        self.fromApiKey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your TM API-key...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"API-KEY \u043a\u0443\u0434\u0430 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u043c", None))
        self.toApiKey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your TM API-key...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0432 \u0440\u0443\u0431\u043b\u044f\u0445", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0432 \u043a\u043e\u043f\u0435\u0439\u043a\u0430\u0445", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u0432\u044b \u043d\u0435 \u0432\u0432\u0435\u0434\u0435\u0442\u0435 \u0441\u0443\u043c\u043c\u0443, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u043f\u0435\u0440\u0435\u043d\u0435\u0441\u0435\u043d \u0432\u0435\u0441\u044c \u0431\u0430\u043b\u0430\u043d\u0441 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.paymentPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your payment password...", None))
        self.PaymentLinkLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://market.csgo.com/checkout/password\"><span style=\" text-decoration: underline; color:#0000ff;\">\u0413\u0434\u0435 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c?</span></a></p></body></html>", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.body.setTabText(self.body.indexOf(self.TM), QCoreApplication.translate("MainWindow", u"TM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"API-KEY \u043e\u0442\u043a\u0443\u0434\u0430 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u043c", None))
        self.fromWaxKey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your WaxPeer API-key...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SteamID \u043a\u0443\u0434\u0430 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u043c", None))
        self.steamId.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your SteamID(7656....)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0432 $", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0432 \u0446\u0435\u043d\u0442\u0430\u0445", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u0432\u044b \u043d\u0435 \u0432\u0432\u0435\u0434\u0435\u0442\u0435 \u0441\u0443\u043c\u043c\u0443, \u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u043f\u0435\u0440\u0435\u043d\u0435\u0441\u0435\u043d \u0432\u0435\u0441\u044c \u0431\u0430\u043b\u0430\u043d\u0441 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.sendButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0442\u0438 \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.body.setTabText(self.body.indexOf(self.waxPage), QCoreApplication.translate("MainWindow", u"WaxPeer", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
        self.creditLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0410\u0432\u0442\u043e\u0440: <a href=\"https://vk.com/tern.trade\"><span style=\" text-decoration: underline; color:#0000ff;\">https://vk.com/tern.trade</span></a></p></body></html>", None))
    # retranslateUi

