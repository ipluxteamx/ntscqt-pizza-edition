# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/configExportDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TemplateConfigDialog(object):
    def setupUi(self, TemplateConfigDialog):
        TemplateConfigDialog.setObjectName("TemplateConfigDialog")
        TemplateConfigDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(TemplateConfigDialog)
        self.buttonBox.setGeometry(QtCore.QRect(252, 240, 140, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.configJsonTextField = QtWidgets.QPlainTextEdit(TemplateConfigDialog)
        self.configJsonTextField.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.configJsonTextField.setObjectName("configJsonTextField")
        self.copyConfigButton = QtWidgets.QPushButton(TemplateConfigDialog)
        self.copyConfigButton.setGeometry(QtCore.QRect(10, 240, 228, 51))
        self.copyConfigButton.setObjectName("copyConfigButton")

        self.retranslateUi(TemplateConfigDialog)
        self.buttonBox.rejected.connect(TemplateConfigDialog.reject)
        self.buttonBox.accepted.connect(TemplateConfigDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(TemplateConfigDialog)

    def retranslateUi(self, TemplateConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        TemplateConfigDialog.setWindowTitle(_translate("TemplateConfigDialog", "Dialog"))
        self.copyConfigButton.setText(_translate("TemplateConfigDialog", "Copy"))
