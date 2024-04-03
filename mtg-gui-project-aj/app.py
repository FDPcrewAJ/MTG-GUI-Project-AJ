import sys

from PyQt6.QtGui import QFont
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

        main_layout = QVBoxLayout()
        selector_layout = QHBoxLayout()
        widgets = [
            QLabel,
            QListWidget,
            QPushButton,
        ]


        # Assign each widget a variable
        title_label = QLabel("Magic: The Gathering Commander Finder")
        color_selector = QListWidget()
        color_selector.addItems(["White", "Blue", "Black", "Red", "Green", "Colorless"])
        info_text = QLabel("Select which colors you want on your commander, or select none for a completely random card!")
        search_button = QPushButton("Find a Commander!")
        card_text = "Your Commander is:"
        card_return = QLabel(card_text)


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


app = QApplication(sys.argv)
app.setStyle("Fusion")
app.setFont(QFont("Calibri", 10))
window = MainWindow()
window.show()

app.exec()
