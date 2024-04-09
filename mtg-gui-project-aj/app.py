import sys

from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QListWidget, QAbstractItemView
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
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
        
        color_selector = QListWidget(self)
        color_selector.addItems(["White", "Blue", "Black", "Red", "Green", "Colorless"])
        color_selector.setFont(QFont("Bellefair"))
        """Selection of multiple items in a list came from https://stackoverflow.com/questions/4008649/qlistwidget-and-multiple-selection"""
        color_selector.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        info_text = QLabel("Select which colors you want on your commander, or select none for a completely random card!")
        info_text.setFont(QFont("Bellefair"))
        search_button = QPushButton("Find a Commander!")
        search_button.setFont(QFont("Fondamento"))
        card_text = "Your Commander is:"
        card_name = "_________"
        card_return = QLabel(f"{card_text} \n {card_name}")
        card_return.setFont(QFont("Bellefair"))


        # Add the widget variables to the window
        main_layout.addWidget(title_label)
        main_layout.addLayout(selector_layout)
        selector_layout.addWidget(color_selector)
        selector_layout.addWidget(info_text)
        main_layout.addWidget(search_button)
        main_layout.addWidget(card_return)
    

        
        widget = QWidget()
        widget.setLayout(main_layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    
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
