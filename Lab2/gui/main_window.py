# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eyazis2_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_widget.setObjectName("main_widget")
        self.main_widget.setStyleSheet("""
            QWidget {
                background-color: #333;
                color: #FFFFFF;
                border: 2px solid #007ACC;
                border-radius: 10px;
                padding: 10px;
            }

            QWidget:hover {
                background-color: #444;
                border: 2px solid #005C99;
            }

            QWidget:selected {
                background-color: #007ACC;
                color: #FFFFFF;
            }

            QWidget:disabled {
                background-color: #666;
                color: #888;
                border: 2px solid #666;
            }

            QWidget QPushButton {
                background-color: #007ACC;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
            }

            QWidget QPushButton:hover {
                background-color: #005C99;
            }

            QWidget QPushButton:pressed {
                background-color: #003D66;
            }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_file_path_frame = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_file_path_frame.sizePolicy().hasHeightForWidth())
        self.l_file_path_frame.setSizePolicy(sizePolicy)
        self.l_file_path_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_file_path_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_file_path_frame.setObjectName("l_file_path_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.l_file_path_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_file_path_label = QtWidgets.QLabel(self.l_file_path_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_file_path_label.sizePolicy().hasHeightForWidth())
        self.l_file_path_label.setSizePolicy(sizePolicy)
        self.l_file_path_label.setObjectName("l_file_path_label")


        self.horizontalLayout.addWidget(self.l_file_path_label)
        self.l_file_path_text = QtWidgets.QPlainTextEdit(self.l_file_path_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_file_path_text.sizePolicy().hasHeightForWidth())
        self.l_file_path_text.setSizePolicy(sizePolicy)
        self.l_file_path_text.setObjectName("l_file_path_text")
        self.horizontalLayout.addWidget(self.l_file_path_text)
        self.l_file_path_browse_btn = QtWidgets.QPushButton(self.l_file_path_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_file_path_browse_btn.sizePolicy().hasHeightForWidth())
        self.l_file_path_browse_btn.setSizePolicy(sizePolicy)
        self.l_file_path_browse_btn.setObjectName("l_file_path_browse_btn")
        self.l_file_path_browse_btn.setStyleSheet("""
                    QPushButton {
                        background-color: purple;
                        border: none;
                        border-radius: 10px;
                        color: white;
                        padding: 10px 20px;
                    }

                    QPushButton:hover {
                        background-color: darkpurple;
                    }

                    QPushButton:pressed {
                        background-color: violet;
                    }
                """)
        self.horizontalLayout.addWidget(self.l_file_path_browse_btn)
        self.verticalLayout.addWidget(self.l_file_path_frame)
        self.l_method_frame = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_method_frame.sizePolicy().hasHeightForWidth())
        self.l_method_frame.setSizePolicy(sizePolicy)
        self.l_method_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_method_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.l_method_frame.setObjectName("l_method_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.l_method_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_method_label_2 = QtWidgets.QLabel(self.l_method_frame)
        self.l_method_label_2.setObjectName("l_method_label_2")
        self.horizontalLayout_2.addWidget(self.l_method_label_2)
        self.l_mode_combo_box = QtWidgets.QComboBox(self.l_method_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_mode_combo_box.sizePolicy().hasHeightForWidth())
        self.l_mode_combo_box.setSizePolicy(sizePolicy)
        self.l_mode_combo_box.setObjectName("l_mode_combo_box")
        self.l_mode_combo_box.setStyleSheet("""
            QComboBox {
                background-color: #444;
                color: #FFFFFF;
                border: 2px solid #007ACC;
                border-radius: 5px;
                padding: 5px;
                selection-background-color: #007ACC;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 2px solid #007ACC;
                background-color: #007ACC;
            }

            QComboBox QAbstractItemView {
                background-color: #333;
                color: #FFFFFF;
                border: 1px solid #007ACC;
                selection-background-color: #007ACC;
            }

            QComboBox QAbstractItemView::item:hover {
                background-color: #444;
            }

            QComboBox QAbstractItemView::item:selected {
                background-color: #007ACC;
                color: #FFFFFF;
            }
        """)

        self.horizontalLayout_2.addWidget(self.l_mode_combo_box)
        self.l_method_label_1 = QtWidgets.QLabel(self.l_method_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_method_label_1.sizePolicy().hasHeightForWidth())
        self.l_method_label_1.setSizePolicy(sizePolicy)
        self.l_method_label_1.setObjectName("l_method_label_1")
        self.horizontalLayout_2.addWidget(self.l_method_label_1)
        self.l_method_combo_box = QtWidgets.QComboBox(self.l_method_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_method_combo_box.sizePolicy().hasHeightForWidth())
        self.l_method_combo_box.setSizePolicy(sizePolicy)
        self.l_method_combo_box.setObjectName("l_method_combo_box")
        self.l_method_combo_box.setStyleSheet("""
                   QComboBox {
                       background-color: #444;
                       color: #FFFFFF;
                       border: 2px solid #007ACC;
                       border-radius: 5px;
                       padding: 5px;
                       selection-background-color: #007ACC;
                   }

                   QComboBox::drop-down {
                       subcontrol-origin: padding;
                       subcontrol-position: top right;
                       width: 20px;
                       border-left: 2px solid #007ACC;
                       background-color: #007ACC;
                   }

                   QComboBox QAbstractItemView {
                       background-color: #333;
                       color: #FFFFFF;
                       border: 1px solid #007ACC;
                       selection-background-color: #007ACC;
                   }

                   QComboBox QAbstractItemView::item:hover {
                       background-color: #444;
                   }

                   QComboBox QAbstractItemView::item:selected {
                       background-color: #007ACC;
                       color: #FFFFFF;
                   }
               """)
        self.horizontalLayout_2.addWidget(self.l_method_combo_box)
        self.l_method_start_btn = QtWidgets.QPushButton(self.l_method_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_method_start_btn.sizePolicy().hasHeightForWidth())
        self.l_method_start_btn.setSizePolicy(sizePolicy)
        self.l_method_start_btn.setObjectName("l_method_start_btn")
        self.l_method_start_btn.setStyleSheet("""
            QPushButton {
                background-color: purple;
                border: none;
                border-radius: 10px;
                color: white;
                padding: 10px 20px;
            }

            QPushButton:hover {
                background-color: darkpurple;
            }

            QPushButton:pressed {
                background-color: violet;
            }
        """)
        self.horizontalLayout_2.addWidget(self.l_method_start_btn)
        self.verticalLayout.addWidget(self.l_method_frame)
        self.local_text_browser = QtWidgets.QTextBrowser(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local_text_browser.sizePolicy().hasHeightForWidth())
        self.local_text_browser.setSizePolicy(sizePolicy)
        self.local_text_browser.setObjectName("local_text_browser")
        self.verticalLayout.addWidget(self.local_text_browser)
        MainWindow.setCentralWidget(self.main_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 724, 25))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        self.menuFIle = QtWidgets.QMenu(self.menu_bar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menu_bar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.menu_help.addAction(self.action_about)
        self.menuFIle.addAction(self.action_save_as)
        self.menu_bar.addAction(self.menuFIle.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Language recognition"))
        self.l_file_path_label.setText(_translate("MainWindow", "Source"))
        self.l_file_path_browse_btn.setText(_translate("MainWindow", "Browse"))
        self.l_method_label_2.setText(_translate("MainWindow", "Mode  "))
        self.l_method_label_1.setText(_translate("MainWindow", "Method"))
        self.l_method_start_btn.setText(_translate("MainWindow", "Start"))
        self.local_text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu_help.setTitle(_translate("MainWindow", "&Help"))
        self.menuFIle.setTitle(_translate("MainWindow", "&FIle"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_save_as.setText(_translate("MainWindow", "Save As..."))

