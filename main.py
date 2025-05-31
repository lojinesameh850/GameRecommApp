import sys
import platform

from modules import *
from widgets import *

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QScrollArea, QWidget

import mockBackend

widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        title = "PlayBud"
        description = "Get game recommendations based on your preferences!"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_allGames.clicked.connect(self.buttonClick)
        widgets.btn_generate_recommendations.clicked.connect(self.buttonClick)
        self.show()
        
        useCustomTheme = False
        themeFile = "theme.qss"

        if useCustomTheme:
            UIFunctions.theme(self, themeFile, True)
            AppFunctions.setThemeHack(self)

        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # Here are functions for clicked buttons
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_allGames":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName == "btn_generate_recommendations":
            answers = {
                "age":widgets.label_age_value.text().lower(),  # ['child','teen','adult']
                "genre":widgets.combo_genre.currentText().lower(),  # ['rpg','shooter','puzzle','platformer','sports','horror','adventure']
                "platform":widgets.combo_platform.currentText().lower(),  # ['pc','console','mobile']
                "session_length":widgets.label_time_value.text().lower(),  # ['short','medium','long']
                "game_mode":widgets.combo_mode.currentText().lower(),  # ['multiplayer','singleplayer']
                "violence":"yes" if widgets.radio_violence_yes.isChecked() else "no",  # ['yes','no']
                "graphics":widgets.combo_graphics.currentText().lower(),  # ['realistic','stylized','retro']
                "story":widgets.label_story_value.text().lower(),  # ['low','medium','high']
                "budget":widgets.label_budget_value.text().lower(),  # ['free','cheap','pricey']
                "online":"yes" if widgets.radio_online_yes .isChecked() else "no",  # ['yes','no']
                "skill":widgets.label_experience_value.text().lower()  # ['beginner','intermediate','expert']
            }
            if answers["session_length"]=="medium (3-4h)":
                answers["session_length"]="medium"
            elif answers["session_length"]=="long (5h+)":
                answers["session_length"]="long"
            elif answers["session_length"]=="short (1-2h)":
                answers["session_length"]="short"

            if answers["age"]=="child (3-12)":
                answers["age"]="child"
            elif answers["age"]=="teen (13-19)":
                answers["age"]="teen"
            elif answers["age"]=="adult (20+)":
                answers["age"]="adult"
            
            if answers["budget"]=="free (0$)":
                answers["budget"]="free"
            elif answers["budget"]=="cheap (- $50)":
                answers["budget"]="cheap"
            elif answers["budget"]=="pricey ($50+)":
                answers["budget"]="pricey"

            print("Generating recommendations with answers:", answers)
            backendResult=mockBackend.result(answers)
            print("Recommendations:", backendResult)
            self.recommendations_window = RecommendationsWindow(backendResult, self)
            self.recommendations_window.exec_()
        print(f'Button "{btnName}" pressed!')
        

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


class RecommendationsWindow(QDialog):
    def __init__(self, recommendations, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Recommendations")
        self.setMinimumSize(400, 300)

        
        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a container widget for the scroll area
        container = QWidget()
        layout = QVBoxLayout(container)

        # Add a title label
        label_title = QLabel("Recommended Games:")
        label_title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(label_title)

        # Add each recommendation with an image
        for game in recommendations["recommended"]:
            # Create a horizontal layout for the image and game name
            game_layout = QHBoxLayout()

            # Add an image (placeholder or actual image path)
            image_label = QLabel()
            image_label.setFixedSize(80, 80)  # Increased image size
            image_label.setStyleSheet("border: 1px solid gray;")  # Optional: Add a border
            image_label.setPixmap(QPixmap("path/to/placeholder.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))  # Replace with actual image path

            # Add the game name
            game_name_label = QLabel(game)
            game_name_label.setStyleSheet("font-size: 16px; margin-left: 10px;")  # Increased font size

            # Add the image and game name to the horizontal layout
            game_layout.addWidget(image_label)
            game_layout.addWidget(game_name_label)

            # Add the horizontal layout to the main layout
            layout.addLayout(game_layout)

        # Set the container widget as the scroll area's widget
        scroll_area.setWidget(container)

        # Create the main layout for the dialog
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
