import sys
from PySide6.QtWidgets import (
    QApplication,
    QFontDialog,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class FontChooser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('font selection')

        layout = QVBoxLayout()
        self.setLayout(layout)

        but_font = QPushButton('Select Font')
        but_font.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        but_font.clicked.connect(self.font_selected)
        layout.addWidget(but_font)

    def font_selected(self):
        button: QPushButton = self.sender()
        ok, font = QFontDialog.getFont()
        if ok:
            button.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = FontChooser()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
