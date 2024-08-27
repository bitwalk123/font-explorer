import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPlainTextEdit,
    QStyle,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class FontChooser(QMainWindow):
    __version__ = '1.0.0'
    # CSS
    style_panel = """
      QPlainTextEdit {
        padding: 0.2em;
        font-family: %s;
        font-size: 32px;
        color: Navy;
        background-color: Ivory;
      }
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font Explorer')
        self.resize(450, 250)

        toolbar = QToolBar()
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

        but_open = QToolButton()
        pixmap_icon = QStyle.StandardPixmap.SP_DirIcon
        icon = self.style().standardIcon(pixmap_icon)
        but_open.setIcon(icon)
        but_open.clicked.connect(self.on_open)
        toolbar.addWidget(but_open)

        base = QWidget()
        self.setCentralWidget(base)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        base.setLayout(layout)

        self.pte_font = pte_font = QPlainTextEdit()
        pte_font.setStyleSheet(self.style_panel % 'sans-serif')
        layout.addWidget(pte_font)

    def on_open(self):
        dialog = QFileDialog()
        dialog.setNameFilters(['Font files (*.ttf *.otf)'])
        if not dialog.exec():
            return
        fontfile = dialog.selectedFiles()[0]
        self.setWindowTitle(os.path.basename(fontfile))
        id = QFontDatabase.addApplicationFont(fontfile)
        family = QFontDatabase.applicationFontFamilies(id)[0]
        self.pte_font.setStyleSheet(self.style_panel % family)


def main():
    app = QApplication(sys.argv)
    ex = FontChooser()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
