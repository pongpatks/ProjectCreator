# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

#---------------------------------------------------------------------------------------------------------------------------------------------
#
# Burak Ertekin - 26/02/2016
# Version 0.4.0
# My Liaison Project Creator
# 0.2.1 - added input/output file synchronization feature for color grading tab
# 0.2.2 - added audio and artworks buttons for grading 
# 0.2.4 - added first archive feature
# 0.3.4 - color grading tab replaced by archiving tab
# 0.4.0 - changed tool name from Cherry Cherry to My Liaison
#
#---------------------------------------------------------------------------------------------------------------------------------------------

import sys
import os
from PyQt5 import QtCore, QtWidgets, QtGui

serverPath = 'M:/JOBS/'
imagePath = 'MYL_logo.png'
#'newCCprojectCreator_02.png'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_CCProjectCreator(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(542, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(542, 290))
        MainWindow.setMaximumSize(QtCore.QSize(542, 290))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        MainWindow.setWindowIcon(QtGui.QIcon('MYL_s_logo.png'))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.vboxlayout = QtWidgets.QVBoxLayout(self.centralWidget)
        #self.vboxlayout.setMargin(11)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_createJob = QtWidgets.QWidget()
        self.tab_createJob.setObjectName(_fromUtf8("tab_createJob"))
        self.button_structure = QtWidgets.QPushButton(self.tab_createJob)
        self.button_structure.setGeometry(QtCore.QRect(330, 90, 131, 23))
        self.button_structure.setObjectName(_fromUtf8("button_structure"))
        self.label = QtWidgets.QLabel(self.tab_createJob)
        self.label.setGeometry(QtCore.QRect(130, 30, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        
        cherry = QtWidgets.QLabel(self.tab_createJob)
        
        pixmap = QtGui.QPixmap(imagePath)
        #cherry.move(85,135)
        cherry.move(130, 140)
        cherry.setPixmap(pixmap)
        
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        cherry.setPalette(palette)

        self.jobNameLineEdit = QtWidgets.QLineEdit(self.tab_createJob)
        self.jobNameLineEdit.setGeometry(QtCore.QRect(130, 60, 331, 20))
        self.jobNameLineEdit.setObjectName(_fromUtf8("jobNameLineEdit"))
        self.jobNameLabel = QtWidgets.QLabel(self.tab_createJob)
        self.jobNameLabel.setGeometry(QtCore.QRect(61, 60, 54, 16))
        self.jobNameLabel.setObjectName(_fromUtf8("jobNameLabel"))
        self.serverLabel = QtWidgets.QLabel(self.tab_createJob)
        self.serverLabel.setGeometry(QtCore.QRect(61, 31, 39, 16))
        self.serverLabel.setObjectName(_fromUtf8("serverLabel"))
        self.tabWidget.addTab(self.tab_createJob, _fromUtf8(""))
        self.tab_createSequence = QtWidgets.QWidget()
        self.tab_createSequence.setObjectName(_fromUtf8("tab_createSequence"))



        self.button_createSequence = QtWidgets.QPushButton(self.tab_createSequence)
        self.button_createSequence.setGeometry(QtCore.QRect(320, 130, 141, 23))
        self.button_createSequence.setObjectName(_fromUtf8("button_createSequence"))
        self.shotNumbersLabel = QtWidgets.QLabel(self.tab_createSequence)
        self.shotNumbersLabel.setGeometry(QtCore.QRect(61, 100, 74, 16))
        self.shotNumbersLabel.setObjectName(_fromUtf8("shotNumbersLabel"))
        self.shotNumbersLineEdit = QtWidgets.QLineEdit(self.tab_createSequence)
        self.shotNumbersLineEdit.setGeometry(QtCore.QRect(151, 100, 311, 20))
        self.shotNumbersLineEdit.setObjectName(_fromUtf8("shotNumbersLineEdit"))
        self.sequenceNameLineEdit = QtWidgets.QLineEdit(self.tab_createSequence)
        self.sequenceNameLineEdit.setGeometry(QtCore.QRect(151, 75, 311, 19))
        self.sequenceNameLineEdit.setObjectName(_fromUtf8("sequenceNameLineEdit"))
        self.sequenceNameLabel = QtWidgets.QLabel(self.tab_createSequence)
        self.sequenceNameLabel.setGeometry(QtCore.QRect(61, 75, 84, 16))
        self.sequenceNameLabel.setObjectName(_fromUtf8("sequenceNameLabel"))
        self.jobNameLabel_2 = QtWidgets.QLabel(self.tab_createSequence)
        self.jobNameLabel_2.setGeometry(QtCore.QRect(61, 50, 54, 16))
        self.jobNameLabel_2.setObjectName(_fromUtf8("jobNameLabel_2"))
        self.serverWidget_2 = QtWidgets.QWidget(self.tab_createSequence)
        self.serverWidget_2.setGeometry(QtCore.QRect(151, 31, 110, 16))
        self.serverWidget_2.setObjectName(_fromUtf8("serverWidget_2"))
        self.label_2 = QtWidgets.QLabel(self.serverWidget_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.jobNameComboBox = QtWidgets.QComboBox(self.tab_createSequence)
        self.jobNameComboBox.setGeometry(QtCore.QRect(151, 50, 311, 19))
        self.jobNameComboBox.setObjectName(_fromUtf8("jobNameComboBox"))
        self.serverLabel_2 = QtWidgets.QLabel(self.tab_createSequence)
        self.serverLabel_2.setGeometry(QtCore.QRect(61, 31, 39, 16))
        self.serverLabel_2.setObjectName(_fromUtf8("serverLabel_2"))
        self.tabWidget.addTab(self.tab_createSequence, _fromUtf8(""))
        self.tab_addShots = QtWidgets.QWidget()
        self.tab_addShots.setObjectName(_fromUtf8("tab_addShots"))



        self.button_addShots = QtWidgets.QPushButton(self.tab_addShots)
        self.button_addShots.setGeometry(QtCore.QRect(320, 130, 141, 23))
        self.button_addShots.setObjectName(_fromUtf8("button_addShots"))
        self.shotNumbersLineEdit_2 = QtWidgets.QLineEdit(self.tab_addShots)
        self.shotNumbersLineEdit_2.setGeometry(QtCore.QRect(151, 102, 311, 20))
        self.shotNumbersLineEdit_2.setObjectName(_fromUtf8("shotNumbersLineEdit_2"))
        self.shotNumbersLabel_2 = QtWidgets.QLabel(self.tab_addShots)
        self.shotNumbersLabel_2.setGeometry(QtCore.QRect(61, 102, 74, 16))
        self.shotNumbersLabel_2.setObjectName(_fromUtf8("shotNumbersLabel_2"))
        self.sequenceNameComboBox = QtWidgets.QComboBox(self.tab_addShots)
        self.sequenceNameComboBox.setGeometry(QtCore.QRect(151, 76, 311, 20))
        self.sequenceNameComboBox.setObjectName(_fromUtf8("sequenceNameComboBox"))
        self.sequenceNameLabel_2 = QtWidgets.QLabel(self.tab_addShots)
        self.sequenceNameLabel_2.setGeometry(QtCore.QRect(61, 76, 84, 16))
        self.sequenceNameLabel_2.setObjectName(_fromUtf8("sequenceNameLabel_2"))
        self.jobNameLabel_3 = QtWidgets.QLabel(self.tab_addShots)
        self.jobNameLabel_3.setGeometry(QtCore.QRect(61, 50, 54, 16))
        self.jobNameLabel_3.setObjectName(_fromUtf8("jobNameLabel_3"))
        self.serverWidget_3 = QtWidgets.QWidget(self.tab_addShots)
        self.serverWidget_3.setGeometry(QtCore.QRect(151, 31, 110, 16))
        self.serverWidget_3.setObjectName(_fromUtf8("serverWidget_3"))
        self.label_3 = QtWidgets.QLabel(self.serverWidget_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.jobNameComboBox_2 = QtWidgets.QComboBox(self.tab_addShots)
        self.jobNameComboBox_2.setGeometry(QtCore.QRect(151, 50, 311, 20))
        self.jobNameComboBox_2.setObjectName(_fromUtf8("jobNameComboBox_2"))
        self.serverLabel_3 = QtWidgets.QLabel(self.tab_addShots)
        self.serverLabel_3.setGeometry(QtCore.QRect(61, 31, 39, 16))
        self.serverLabel_3.setObjectName(_fromUtf8("serverLabel_3"))
        self.tabWidget.addTab(self.tab_addShots, _fromUtf8(""))
        self.tab_shotgunIntegration = QtWidgets.QWidget()
        self.tab_shotgunIntegration.setObjectName(_fromUtf8("tab_shotgunIntegration"))



        self.button_browseConfig = QtWidgets.QPushButton(self.tab_shotgunIntegration)
        self.button_browseConfig.setGeometry(QtCore.QRect(470, 70, 21, 16))
        self.button_browseConfig.setObjectName(_fromUtf8("button_browseConfig"))
        self.button_updateConfig = QtWidgets.QPushButton(self.tab_shotgunIntegration)
        self.button_updateConfig.setGeometry(QtCore.QRect(370, 100, 91, 23))
        self.button_updateConfig.setObjectName(_fromUtf8("button_updateConfig"))
        self.configLocationLabel = QtWidgets.QLabel(self.tab_shotgunIntegration)
        self.configLocationLabel.setGeometry(QtCore.QRect(61, 65, 81, 16))
        self.configLocationLabel.setObjectName(_fromUtf8("configLocationLabel"))
        self.jobNameComboBox_3 = QtWidgets.QComboBox(self.tab_shotgunIntegration)
        self.jobNameComboBox_3.setGeometry(QtCore.QRect(148, 35, 311, 20))
        self.jobNameComboBox_3.setObjectName(_fromUtf8("jobNameComboBox_3"))
        self.configLocationLineEdit = QtWidgets.QLineEdit(self.tab_shotgunIntegration)
        self.configLocationLineEdit.setGeometry(QtCore.QRect(148, 65, 311, 20))
        self.configLocationLineEdit.setObjectName(_fromUtf8("configLocationLineEdit"))
        self.jobNameLabel_4 = QtWidgets.QLabel(self.tab_shotgunIntegration)
        self.jobNameLabel_4.setGeometry(QtCore.QRect(61, 35, 54, 16))
        self.jobNameLabel_4.setObjectName(_fromUtf8("jobNameLabel_4"))
        self.tabWidget.addTab(self.tab_shotgunIntegration, _fromUtf8(""))
        
        self.tab_archive = QtWidgets.QWidget()
        self.tab_archive.setObjectName(_fromUtf8("tab_archive"))
        self.archiveProjectNameLabel = QtWidgets.QLabel(self.tab_archive)
        self.archiveProjectNameLabel.setGeometry(QtCore.QRect(61, 35, 54, 16))
        self.archiveProjectNameLabel.setObjectName(_fromUtf8("archiveProjectNameLabel"))
        self.archiveSequenceNameLabel = QtWidgets.QLabel(self.tab_archive)
        self.archiveSequenceNameLabel.setGeometry(QtCore.QRect(61,65,81,16))
        self.archiveSequenceNameLabel.setObjectName(_fromUtf8("archiveSequenceNameLabel"))
        self.archiveProjectComboBox = QtWidgets.QComboBox(self.tab_archive)
        self.archiveProjectComboBox.setGeometry(QtCore.QRect(148, 35, 311, 20))
        self.archiveProjectComboBox.setObjectName(_fromUtf8("archiveProjectComboBox"))
        self.archiveSequenceComboBox = QtWidgets.QComboBox(self.tab_archive)
        self.archiveSequenceComboBox.setGeometry(QtCore.QRect(148,65,311,20))
        self.archiveSequenceComboBox.setObjectName(_fromUtf8("archiveSequenceComboBox"))
        self.button_archive = QtWidgets.QPushButton(self.tab_archive)
        self.button_archive.setGeometry(QtCore.QRect(298, 100, 160, 24))
        self.button_archive.setObjectName(_fromUtf8("button_archive"))
        self.archiveShotNameLabel = QtWidgets.QLabel(self.tab_archive)
        self.archiveShotNameLabel.setGeometry(QtCore.QRect(61, 95, 81, 16))
        self.archiveShotNameLabel.setObjectName(_fromUtf8("archiveShotNameLabel"))
        self.archiveShotComboBox = QtWidgets.QComboBox(self.tab_archive)
        self.archiveShotComboBox.setGeometry(QtCore.QRect(148, 95, 130, 20))
        self.archiveShotComboBox.setObjectName(_fromUtf8("archiveShotComboBox"))
        self.tabWidget.addTab(self.tab_archive, _fromUtf8(""))

        self.vboxlayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "My Liaison Project Creator", None))
        self.button_structure.setText(_translate("MainWindow", "Create Jobs Structure", None))
        self.label.setText(_translate("MainWindow", serverPath, None))
        self.jobNameLabel.setText(_translate("MainWindow", "Job Name: ", None))
        self.serverLabel.setText(_translate("MainWindow", "Server: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_createJob), _translate("MainWindow", "Create Job", None))
        self.button_createSequence.setText(_translate("MainWindow", "Add Shot-Database", None))
        self.shotNumbersLabel.setText(_translate("MainWindow", "Shot Numbers: ", None))
        self.sequenceNameLabel.setText(_translate("MainWindow", "Sequence Name: ", None))
        self.jobNameLabel_2.setText(_translate("MainWindow", "Job Name: ", None))
        self.label_2.setText(_translate("MainWindow", serverPath, None))
        self.serverLabel_2.setText(_translate("MainWindow", "Server: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_createSequence), _translate("MainWindow", "Create Sequence", None))
        self.button_addShots.setText(_translate("MainWindow", "Add Shots", None))
        self.shotNumbersLabel_2.setText(_translate("MainWindow", "Shot Numbers: ", None))
        self.sequenceNameLabel_2.setText(_translate("MainWindow", "Sequence Name: ", None))
        self.jobNameLabel_3.setText(_translate("MainWindow", "Job Name: ", None))
        self.label_3.setText(_translate("MainWindow", serverPath, None))
        self.serverLabel_3.setText(_translate("MainWindow", "Server: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_addShots), _translate("MainWindow", "Add Shots", None))
        self.button_browseConfig.setText(_translate("MainWindow", "...", None))
        self.button_updateConfig.setText(_translate("MainWindow", "Update Config", None))
        self.configLocationLabel.setText(_translate("MainWindow", "Config Location: ", None))
        self.configLocationLineEdit.setPlaceholderText(_translate("MainWindow", "Y:/SHOTGUN/main_config/config", None))
        self.configLocationLineEdit.setText("Y:/SHOTGUN/main_config/config")
        self.jobNameLabel_4.setText(_translate("MainWindow", "Job Name: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_shotgunIntegration), _translate("MainWindow", "Shotgun Integration", None))
        self.button_archive.setText(_translate("MainWindow", "Clean", None))
        self.archiveProjectNameLabel.setText(_translate("MainWindow", "Job Name: ", None))
        self.archiveSequenceNameLabel.setText(_translate("MainWindow", "Sequence Name: ", None))
        self.archiveShotNameLabel.setText(_translate("MainWindow", "Shot Name: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_archive), _translate("MainWindow", "Cleaning", None))