import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MTG Commander Finder")
        self.setContentsMargins(10, 10, 10, 10)
        self.resize(480, 640)

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QLabel,
            QPushButton,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()

app.exec()
