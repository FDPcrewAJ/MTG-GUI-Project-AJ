import controller
import sys

from PyQt6.QtGui import QFontDatabase, QFont
import PyQt6.QtCore
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QListWidget,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MTG Commander Finder")
        self.setContentsMargins(10, 10, 10, 10)
        self.resize(480, 640)
        
        # Load fonts
        self.set_fonts("Bellefair-Regular.ttf")
        self.set_fonts("Fondamento-Regular.ttf")

        main_layout = QVBoxLayout()
        selector_layout = QHBoxLayout()
        widgets = [
            QLabel,
            QListWidget,
            QPushButton,
        ]


        # Assign each widget a variable
        title_label = QLabel("Magic: The Gathering Commander Finder")
        title_label.setFont(QFont("Fondamento", 20))
        title_label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Color selection QListWidget setup
        self.color_selector = QListWidget(self)
        c_white = "White"
        c_blue = "Blue"
        c_black = "Black"
        c_red = "Red"
        c_green = "Green"
        c_colorless = "Colorless"
        self.color_selector.addItem(c_white)
        self.color_selector.addItem(c_blue)
        self.color_selector.addItem(c_black)
        self.color_selector.addItem(c_red)
        self.color_selector.addItem(c_green)
        self.color_selector.addItem(c_colorless)
        self.color_selector.setFont(QFont("Bellefair", 15))
        self.color_selector.setSpacing(11)
        self.color_selector.setMaximumWidth(200)
        self.color_selector.setMinimumWidth(150)
        self.color_selector.setMaximumHeight(300)
        self.color_selector.setMinimumHeight(300)
        """Selection of multiple items in a list came from 
        https://stackoverflow.com/questions/4008649/qlistwidget-and-multiple-selection"""
        self.color_selector.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        # Info Text QLabel setup
        info_text = QLabel(f"Select which colors you want on your commander, or select none for a completely random card! \n*Note: Colorless specifies colorless mana, not generic mana.")
        info_text.setWordWrap(True)
        info_text.setFont(QFont("Bellefair", 20))
        info_text.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)

        # Find commander QPushButton setup
        self.search_button = QPushButton("Find a Commander!")
        self.search_button.setFont(QFont("Fondamento", 25))
        self.search_button.clicked.connect(self.find_user_colors)

        # Card found name Qlabel setup
        card_text = "Your Commander is:"
        card_name = "_________"
        self.card_return = QLabel(f"{card_text} \n {card_name}")
        self.card_return.setFont(QFont("Bellefair", 20))
        self.card_return.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)

        # Add the widget variables to the window
        main_layout.addWidget(title_label)
        main_layout.addLayout(selector_layout)
        selector_layout.addWidget(self.color_selector)
        selector_layout.addWidget(info_text)
        main_layout.addWidget(self.search_button)
        main_layout.addWidget(self.card_return)
    

        
        widget = QWidget()
        widget.setLayout(main_layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    
    def find_user_colors(self):
        # get color inputs from the list widget
        selected_colors = []
        items = self.color_selector.selectedItems()
        for item in range(len(items)):
            selected_colors.append(str(self.color_selector.selectedItems()[item].text()))
        # Call find card function from controller
        print(selected_colors)
        # format results using controller

        # display results


    def set_fonts(self, font_name: str) -> None:
        font_dir = "resources/"
        font_path = font_dir + font_name
        success = QFontDatabase.addApplicationFont(font_path)
        
        # If it failed to set a font path
        if success == -1:
            print(f"{font_name} not loaded: \nTried path {font_path}")


app = QApplication(sys.argv)

stylesheet = None
styles_path = "resources/styles.qss"
# Get the code from the stylesheet
with open(styles_path, "r") as f:
    stylesheet = f.read()
app.setStyleSheet(stylesheet)

app.setStyle("Fusion")
app.setFont(QFont("Calibri", 10))
window = MainWindow()
window.show()

app.exec()
