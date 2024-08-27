import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QRawFont
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget, QMainWindow, QLineEdit, QPlainTextEdit,
)


class FontChooser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font Explorer')

        id_font = QFontDatabase.addApplicationFont('fonts/PopRumKiwi-Telop.ttf')

        base = QWidget()
        self.setCentralWidget(base)

        layout = QVBoxLayout()
        base.setLayout(layout)

        pte_font = QPlainTextEdit()
        family = QFontDatabase.applicationFontFamilies(id_font)[0]
        pte_font.setStyleSheet("""
          QPlainTextEdit{
            font-family: %s;
            font-size: 32px;
            background-color: white;
          }
        """ % family)
        layout.addWidget(pte_font)


def main():
    app = QApplication(sys.argv)
    ex = FontChooser()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
