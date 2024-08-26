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
        self.init_ui()
        self.setWindowTitle('font selection')

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        btn = QPushButton('Select Font')
        btn.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        btn.clicked.connect(self.button_clicked)
        layout.addWidget(btn)

    def button_clicked(self):
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
