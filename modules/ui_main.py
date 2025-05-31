from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(
            "QWidget{\n"
            "    color: rgb(221, 221, 221);\n"
            "    font: 10pt \"Segoe UI\";\n"
            "}\n"
            "\n"
            "QToolTip {\n"
            "    color: #ffffff;\n"
            "    background-color: rgba(33, 37, 43, 180);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    background-image: none;\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 2px solid rgb(255, 121, 198);\n"
            "    text-align: left;\n"
            "    padding-left: 8px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "#bgApp {\n"
            "    background-color: rgb(40, 44, 52);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "#leftMenuBg {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "#topLogo {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    background-image: url(:/images/images/images/playbud_logo.png);\n"
            "    background-position: center 30%;\n"
            "    background-repeat: no-repeat;\n"
            "}\n"
            "\n"
            "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
            "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
            "\n"
            "#topMenu .QPushButton {\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 22px solid transparent;\n"
            "    background-color: transparent;\n"
            "    text-align: left;\n"
            "    padding-left: 44px;\n"
            "}\n"
            "#topMenu .QPushButton:hover {\n"
            "    background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#topMenu .QPushButton:pressed {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "#bottomMenu .QPushButton {\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 20px solid transparent;\n"
            "    background-color:transparent;\n"
            "    text-align: left;\n"
            "    padding-left: 44px;\n"
            "}\n"
            "#bottomMenu .QPushButton:hover {\n"
            "    background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton:pressed {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "#leftMenuFrame{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "#toggleButton {\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 20px solid transparent;\n"
            "    background-color: rgb(37, 41, 48);\n"
            "    text-align: left;\n"
            "    padding-left: 44px;\n"
            "    color: rgb(113, 126, 149);\n"
            "}\n"
            "#toggleButton:hover {\n"
            "    background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#toggleButton:pressed {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "}\n"
            "\n"
            "#titleRightInfo { padding-left: 10px; }\n"
            "\n"
            "#extraLeftBox {\n"
            "    background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#extraTopBg{\n"
            "    background-color: rgb(189, 147, 249)\n"
            "}\n"
            "#extraLabel { color: rgb(255, 255, 255); }\n"
            "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
            "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
            "#extraContent{\n"
            "    border-top: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton {\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 22px solid transparent;\n"
            "    background-color:transparent;\n"
            "    text-align: left;\n"
            "    padding-left: 44px;\n"
            "}\n"
            "#extraTopMenu .QPushButton:hover {\n"
            "    background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton:pressed {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "#contentTopBg{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#contentBottom{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "#bottomBar { background-color: rgb(44, 49, 58); }\n"
            "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "QHeaderView::section{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    max-width: 30px;\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    border-style: none;\n"
            "    border-bottom: 1px solid rgb(44, 49, 60);\n"
            "    border-right: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    border: 1px solid rgb(33, 37, 43);\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    padding: 3px;\n"
            "    border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QLineEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "QPlainTextEdit {\n"
            "    background-color: rgb(27, 29, 35);\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            "}\n"
            "QPlainTextEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "    border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:vertical {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "    border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:vertical {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    height: 20px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    height: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            "}\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
            "}\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "}\n"
            "QComboBox{\n"
            "    background-color: rgb(27, 29, 35);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding: 5px;\n"
            "    padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 25px;\n"
            "    border-left-width: 3px;\n"
            "    border-left-color: rgba(39, 44, 54, 150);\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;\n"
            "    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    color: rgb(255, 121, 198);\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    padding: 10px;\n"
            "    selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "    margin: 0px;\n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "    background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "    background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QCommandLinkButton {\n"
            "    color: rgb(255, 121, 198);\n"
            "    border-radius: 5px;\n"
            "    padding: 5px;\n"
            "    color: rgb(255, 170, 255);\n"
            "}\n"
            "QCommandLinkButton:hover {\n"
            "    color: rgb(255, 170, 255);\n"
            "    background-color: rgb(44, 49, 60);\n"
            "}\n"
            "QCommandLinkButton:pressed {\n"
            "    color: rgb(189, 147, 249);\n"
            "    background-color: rgb(52, 58, 71);\n"
            "}\n"
            "#pagesContainer QPushButton {\n"
            "    border: 2px solid rgb(52, 59, 72);\n"
            "    border-radius: 5px;\n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pagesContainer QPushButton:hover {\n"
            "    background-color: rgb(57, 65, 80);\n"
            "    border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pagesContainer QPushButton:pressed {\n"
            "    background-color: rgb(35, 40, 49);\n"
            "    border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
        )
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_allGames = QPushButton(self.topMenu)
        self.btn_allGames.setObjectName(u"btn_allGames")
        sizePolicy.setHeightForWidth(self.btn_allGames.sizePolicy().hasHeightForWidth())
        self.btn_allGames.setSizePolicy(sizePolicy)
        self.btn_allGames.setMinimumSize(QSize(0, 45))
        self.btn_allGames.setFont(font)
        self.btn_allGames.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_allGames.setLayoutDirection(Qt.LeftToRight)
        self.btn_allGames.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_allGames)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.verticalLayout_5.addLayout(self.extraTopLayout)

        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraColumLayout.addWidget(self.extraContent)

        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"allGames")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # --- User Preferences Form ---
        self.userPrefsFrame = QFrame(self.contentBox)
        self.userPrefsFrame.setObjectName(u"userPrefsFrame")
        self.userPrefsFrame.setFrameShape(QFrame.StyledPanel)
        self.userPrefsFrame.setFrameShadow(QFrame.Raised)
        self.userPrefsLayout = QGridLayout(self.userPrefsFrame)
        self.userPrefsLayout.setObjectName(u"userPrefsLayout")
        
        # Set column widths - labels take 1/3, controls take 2/3
        self.userPrefsLayout.setColumnStretch(0, 1)         # Labels take 1/3 width
        self.userPrefsLayout.setColumnStretch(1, 2)         # Controls take 2/3 width
        
        # Set consistent spacing
        self.userPrefsLayout.setHorizontalSpacing(15)
        self.userPrefsLayout.setVerticalSpacing(12)

        # Helper style for QComboBox popup
        combo_popup_style = (
            "QComboBox {"
            "    max-width: none;"  # Remove max-width restriction
            "}"
            "QComboBox QAbstractItemView {"
            "    background-color: rgb(255, 121, 198);"
            "    color: rgb(255, 255, 255);"
            "}"
        )

        # Custom slider style
        slider_style = (
            "QSlider::groove:horizontal {"
            "    border: 1px solid #999999;"
            "    height: 8px;"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);"
            "    margin: 2px 0;"
            "    border-radius: 4px;"
            "}"
            "QSlider::handle:horizontal {"
            "    background: rgb(255, 121, 198);"
            "    border: 2px solid rgb(255, 121, 198);"
            "    width: 18px;"
            "    margin: -2px 0;"
            "    border-radius: 9px;"
            "}"
            "QSlider::handle:horizontal:hover {"
            "    background: rgb(255, 170, 255);"
            "    border: 2px solid rgb(255, 170, 255);"
            "}"
            "QSlider::handle:horizontal:pressed {"
            "    background: rgb(189, 147, 249);"
            "    border: 2px solid rgb(189, 147, 249);"
            "}"
            "QSlider::sub-page:horizontal {"
            "    background: rgb(255, 121, 198);"
            "    border: 1px solid #777;"
            "    height: 8px;"
            "    border-radius: 4px;"
            "}"
        )

        # Age slider (Young/Adult/Senior - 3 intervals)
        self.label_age = QLabel("Age:")
        self.label_age.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # Left-align in left half
        self.slider_age = QSlider(Qt.Horizontal)
        self.slider_age.setMinimum(0)
        self.slider_age.setMaximum(2)
        self.slider_age.setValue(1)
        self.slider_age.setFixedHeight(25)
        self.slider_age.setStyleSheet(slider_style)
        self.label_age_value = QLabel("Teen (13-19)")
        self.label_age_value.setFixedWidth(100)
        self.label_age_value.setAlignment(Qt.AlignCenter)
        
        def update_age_label(value):
            age_labels = ["Child (3-12)", "Teen (13-19)", "Adult (20+)"]
            self.label_age_value.setText(age_labels[value])
        
        self.slider_age.valueChanged.connect(update_age_label)
        update_age_label(1)  # Set initial text
        
        age_layout = QHBoxLayout()
        age_layout.addWidget(self.slider_age, 1)  # Slider takes most space
        age_layout.addWidget(self.label_age_value, 0)  # Fixed width for label
        self.userPrefsLayout.addWidget(self.label_age, 0, 0)
        self.userPrefsLayout.addLayout(age_layout, 0, 1)

        # Preferred genre
        self.label_genre = QLabel("Preferred genre:")
        self.label_genre.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.combo_genre = QComboBox()
        self.combo_genre.addItems(["RPG", "Shooter", "Puzzle", "Platformer", "Sports", "Horror", "Adventure"])
        self.combo_genre.setFixedSize(220, 30)  # Fixed width for consistency
        self.combo_genre.setStyleSheet(combo_popup_style)
        
        self.userPrefsLayout.addWidget(self.label_genre, 1, 0)
        self.userPrefsLayout.addWidget(self.combo_genre, 1, 1)

        # Gender
        self.label_gender = QLabel("Gender:")
        self.label_gender.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.radio_gender_male = QRadioButton("Male")
        self.radio_gender_female = QRadioButton("Female")
        self.gender_group = QButtonGroup(self.userPrefsFrame)
        self.gender_group.addButton(self.radio_gender_male)
        self.gender_group.addButton(self.radio_gender_female)
        gender_layout = QHBoxLayout()
        gender_layout.setSpacing(200)
        gender_layout.addWidget(self.radio_gender_male)
        gender_layout.addWidget(self.radio_gender_female)
        gender_layout.addStretch()  # Push buttons to left of right half
        self.userPrefsLayout.addWidget(self.label_gender, 2, 0)
        self.userPrefsLayout.addLayout(gender_layout, 2, 1)

        # Time willing to spend (Short/Medium/Long - 3 intervals)
        self.label_time = QLabel("Session length:")
        self.label_time.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.slider_time = QSlider(Qt.Horizontal)
        self.slider_time.setMinimum(0)
        self.slider_time.setMaximum(2)
        self.slider_time.setValue(1)
        self.slider_time.setFixedHeight(25)
        self.slider_time.setStyleSheet(slider_style)
        self.label_time_value = QLabel("Medium")
        self.label_time_value.setFixedWidth(100)
        self.label_time_value.setAlignment(Qt.AlignCenter)
        
        def update_time_label(value):
            time_labels = ["Short (1-2h)", "Medium (3-4h)", "Long (5h+)"]
            self.label_time_value.setText(time_labels[value])
        
        self.slider_time.valueChanged.connect(update_time_label)
        update_time_label(1)  # Set initial text
        
        time_layout = QHBoxLayout()
        time_layout.addWidget(self.slider_time, 1)  # Slider takes most space
        time_layout.addWidget(self.label_time_value, 0)  # Fixed width for label
        self.userPrefsLayout.addWidget(self.label_time, 3, 0)
        self.userPrefsLayout.addLayout(time_layout, 3, 1)

        # Preferred platform
        self.label_platform = QLabel("Preferred platform:")
        self.label_platform.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.combo_platform = QComboBox()
        self.combo_platform.addItems(["PC", "Console", "Mobile"])
        self.combo_platform.setFixedSize(220, 30)
        self.combo_platform.setStyleSheet(combo_popup_style)
        
        self.userPrefsLayout.addWidget(self.label_platform, 4, 0)
        self.userPrefsLayout.addWidget(self.combo_platform, 4, 1)

        # Multiplayer or single-player
        self.label_mode = QLabel("Game mode:")
        self.label_mode.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(["Multiplayer", "Singleplayer"])
        self.combo_mode.setFixedSize(220, 30)
        self.combo_mode.setStyleSheet(combo_popup_style)
        
        self.userPrefsLayout.addWidget(self.label_mode, 5, 0)
        self.userPrefsLayout.addWidget(self.combo_mode, 5, 1)

        # Violence tolerance
        self.label_violence = QLabel("Violence tolerance:")
        self.label_violence.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.radio_violence_yes = QRadioButton("Yes")
        self.radio_violence_no = QRadioButton("No")
        self.violence_group = QButtonGroup(self.userPrefsFrame)
        self.violence_group.addButton(self.radio_violence_yes)
        self.violence_group.addButton(self.radio_violence_no)
        violence_layout = QHBoxLayout()
        violence_layout.setSpacing(200)
        violence_layout.addWidget(self.radio_violence_yes)
        violence_layout.addWidget(self.radio_violence_no)
        violence_layout.addStretch()  # Push buttons to left of right half
        self.userPrefsLayout.addWidget(self.label_violence, 6, 0)
        self.userPrefsLayout.addLayout(violence_layout, 6, 1)

        # Graphics preference
        self.label_graphics = QLabel("Graphics preference:")
        self.label_graphics.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.combo_graphics = QComboBox()
        self.combo_graphics.addItems(["Realistic", "Stylized", "Retro"])
        self.combo_graphics.setFixedSize(220, 30)
        self.combo_graphics.setStyleSheet(combo_popup_style)
        
        self.userPrefsLayout.addWidget(self.label_graphics, 7, 0)
        self.userPrefsLayout.addWidget(self.combo_graphics, 7, 1)

        # Story importance slider (Low/Medium/High - 3 intervals)
        self.label_story = QLabel("Story importance:")
        self.label_story.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.slider_story = QSlider(Qt.Horizontal)
        self.slider_story.setMinimum(0)
        self.slider_story.setMaximum(2)
        self.slider_story.setValue(1)
        self.slider_story.setFixedHeight(25)
        self.slider_story.setStyleSheet(slider_style)
        self.label_story_value = QLabel("Medium")
        self.label_story_value.setFixedWidth(100)
        self.label_story_value.setAlignment(Qt.AlignCenter)
        
        def update_story_label(value):
            story_labels = ["Low", "Medium", "High"]
            self.label_story_value.setText(story_labels[value])
        
        self.slider_story.valueChanged.connect(update_story_label)
        update_story_label(1)  # Set initial text
        
        story_layout = QHBoxLayout()
        story_layout.addWidget(self.slider_story, 1)  # Slider takes most space
        story_layout.addWidget(self.label_story_value, 0)  # Fixed width for label
        self.userPrefsLayout.addWidget(self.label_story, 8, 0)
        self.userPrefsLayout.addLayout(story_layout, 8, 1)

        # Budget slider (Low/Medium/High - 3 intervals)
        self.label_budget = QLabel("Budget:")
        self.label_budget.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.slider_budget = QSlider(Qt.Horizontal)
        self.slider_budget.setMinimum(0)
        self.slider_budget.setMaximum(2)
        self.slider_budget.setValue(1)
        self.slider_budget.setFixedHeight(25)
        self.slider_budget.setStyleSheet(slider_style)
        self.label_budget_value = QLabel("Cheap")
        self.label_budget_value.setFixedWidth(100)
        self.label_budget_value.setAlignment(Qt.AlignCenter)
        
        def update_budget_label(value):
            budget_labels = ["Free", "Cheap (- $50)", "Pricey ($50+)"]
            self.label_budget_value.setText(budget_labels[value])
        
        self.slider_budget.valueChanged.connect(update_budget_label)
        update_budget_label(1)  # Set initial text
        
        budget_layout = QHBoxLayout()
        budget_layout.addWidget(self.slider_budget, 1)  # Slider takes most space
        budget_layout.addWidget(self.label_budget_value, 0)  # Fixed width for label
        self.userPrefsLayout.addWidget(self.label_budget, 9, 0)
        self.userPrefsLayout.addLayout(budget_layout, 9, 1)

        # Online required
        self.label_online = QLabel("Online required?")
        self.label_online.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.radio_online_yes = QRadioButton("Yes")
        self.radio_online_no = QRadioButton("No")
        self.online_group = QButtonGroup(self.userPrefsFrame)
        self.online_group.addButton(self.radio_online_yes)
        self.online_group.addButton(self.radio_online_no)
        online_layout = QHBoxLayout()
        online_layout.setSpacing(200)
        online_layout.addWidget(self.radio_online_yes)
        online_layout.addWidget(self.radio_online_no)
        online_layout.addStretch()  # Push buttons to left of right half
        self.userPrefsLayout.addWidget(self.label_online, 10, 0)
        self.userPrefsLayout.addLayout(online_layout, 10, 1)

        # Experience level slider (Beginner/Intermediate/Expert - 3 intervals)
        self.label_experience = QLabel("Skill level:")
        self.label_experience.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.slider_experience = QSlider(Qt.Horizontal)
        self.slider_experience.setMinimum(0)
        self.slider_experience.setMaximum(2)
        self.slider_experience.setValue(1)
        self.slider_experience.setFixedHeight(25)
        self.slider_experience.setStyleSheet(slider_style)
        self.label_experience_value = QLabel("Intermediate")
        self.label_experience_value.setFixedWidth(100)
        self.label_experience_value.setAlignment(Qt.AlignCenter)
        
        def update_experience_label(value):
            experience_labels = ["Beginner", "Intermediate", "Expert"]
            self.label_experience_value.setText(experience_labels[value])
        
        self.slider_experience.valueChanged.connect(update_experience_label)
        update_experience_label(1)  # Set initial text
        
        experience_layout = QHBoxLayout()
        experience_layout.addWidget(self.slider_experience, 1)  # Slider takes most space
        experience_layout.addWidget(self.label_experience_value, 0)  # Fixed width for label
        self.userPrefsLayout.addWidget(self.label_experience, 11, 0)
        self.userPrefsLayout.addLayout(experience_layout, 11, 1)

        # Add the form to the home page layout (not widgets)
        if hasattr(self, "home"):
            self.home_layout = QVBoxLayout(self.home)
            self.home_layout.setSpacing(10)
            self.home_layout.setObjectName(u"home_layout")
            self.home_layout.setContentsMargins(10, 10, 10, 10)
            self.home_layout.addWidget(self.userPrefsFrame)

            # Add the Generate Recommendations button below the form
            self.btn_generate_recommendations = QPushButton("Generate Recommendations")
            self.btn_generate_recommendations.setObjectName(u"btn_generate_recommendations")
            self.btn_generate_recommendations.setFixedSize(240, 40)
            btn_center_layout = QHBoxLayout()
            btn_center_layout.addStretch()
            btn_center_layout.addWidget(self.btn_generate_recommendations)
            btn_center_layout.addStretch()
            self.home_layout.addLayout(btn_center_layout)
            self.btn_generate_recommendations.setCursor(QCursor(Qt.PointingHandCursor))
            self.btn_generate_recommendations.setStyleSheet(
                "QPushButton {"
                "    background-color: rgb(255, 121, 198);"
                "    color: white;"
                "    border-radius: 8px;"
                "    font: 12pt 'Segoe UI';"
                "}"
                "QPushButton:hover {"
                "    background-color: rgb(255, 170, 255);"
                "}"
                "QPushButton:pressed {"
                "    background-color: rgb(189, 147, 249);"
                "}"
            )
            
        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottomBar)
        self.verticalLayout_2.addWidget(self.contentBottom)
        self.appLayout.addWidget(self.contentBox)
        self.appMargins.addWidget(self.bgApp)
        MainWindow.setCentralWidget(self.styleSheet)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PlayBud", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Game Recommendations", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_allGames.setText(QCoreApplication.translate("MainWindow", u"All games", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PlayBud — Video Game Recommendation System", None))
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        self.closeAppBtn.setText("")

    # retranslateUi