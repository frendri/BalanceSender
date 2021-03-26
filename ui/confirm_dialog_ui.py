# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_dialogLfeZmN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 288)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.from_key = QLabel(self.frame_2)
        self.from_key.setObjectName(u"from_key")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.from_key)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.to_key = QLabel(self.frame_2)
        self.to_key.setObjectName(u"to_key")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.to_key)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.sum = QLabel(self.frame_2)
        self.sum.setObjectName(u"sum")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sum)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.frame_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u0432\u0432\u0435\u0434\u0435\u043d\u044b\u0435 \u0412\u0430\u043c\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421 API-KEY", None))
        self.from_key.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0412 API-KEY", None))
        self.to_key.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.sum.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

